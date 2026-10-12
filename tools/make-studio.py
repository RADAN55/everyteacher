#!/usr/bin/env python3
"""Synthesize the Listening & Speaking Studio audio from tools/studio.py.

Needs sherpa-onnx and the Kokoro English model at $KOKORO
(default ../tts/kokoro-en-v0_19). Writes studio/<clip>.mp3 and
studio/data.json (the content the page renders, with clip durations).

Usage: python3 tools/make-studio.py [clip stems…]
"""
import json, os, re, sys, wave, subprocess
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import studio as S

KOKORO = Path(os.environ.get("KOKORO", ROOT.parent / "tts" / "kokoro-en-v0_19"))
OUT = ROOT / "studio"; OUT.mkdir(exist_ok=True)
SR = 24000
SPEED = {"T": 0.96, "M": 0.95, "A": 1.0, "B": 0.98, "C": 0.94}   # a shade under conversational, test-like


def say(text):
    for a, b in S.SAY:
        text = re.sub(a, b, text)
    return text


def tts():
    import sherpa_onnx
    cfg = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
            model=str(KOKORO / "model.onnx"), voices=str(KOKORO / "voices.bin"),
            tokens=str(KOKORO / "tokens.txt"), data_dir=str(KOKORO / "espeak-ng-data")),
        num_threads=4))
    return sherpa_onnx.OfflineTts(cfg)


def write_wav(path, x):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())


def main(only):
    engine = tts()
    durations = {}
    for stem, turns in S.clips():
        mp3 = OUT / f"{stem}.mp3"
        if only and stem not in only:
            if mp3.exists():
                durations[stem] = probe(mp3)
            continue
        parts, last = [], None
        for who, text in turns:
            a = engine.generate(say(text), sid=S.VOICES[who], speed=SPEED[who])
            x = np.array(a.samples, dtype=np.float32)
            idx = np.where(np.abs(x) > 0.01)[0]
            if len(idx):
                x = x[max(0, idx[0] - int(.05 * SR)): idx[-1] + int(.15 * SR)]
            if last is not None:
                parts.append(np.zeros(int((0.6 if who != last else 0.35) * SR)))
            parts.append(x); last = who
        y = np.concatenate([np.zeros(int(.25 * SR))] + parts + [np.zeros(int(.4 * SR))])
        y = y / max(1e-6, np.percentile(np.abs(y), 99.9)) * 0.7
        wav = OUT / f"{stem}.wav"; write_wav(wav, y)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav),
                        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "24000", "-ac", "1",
                        "-c:a", "libmp3lame", "-b:a", "48k", str(mp3)], check=True)
        wav.unlink()
        durations[stem] = round(len(y) / SR, 1)
        print(f"{stem:14s} {durations[stem]:5.1f}s", flush=True)
    data = {"units": S.UNITS, "dur": durations}
    (OUT / "data.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("wrote studio/data.json")


def probe(mp3):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)],
                       capture_output=True, text=True)
    return round(float(r.stdout.strip() or 0), 1)


if __name__ == "__main__":
    main(set(sys.argv[1:]))
