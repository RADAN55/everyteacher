#!/usr/bin/env python3
"""Synthesize the Every Teacher podcast from tools/podcast.py.

Needs: pip install sherpa-onnx, and the Kokoro English model unpacked at
$KOKORO (default ../tts/kokoro-en-v0_19). Writes podcast/ep-N.mp3 and
podcast/ep-N.json (per-turn timings for the transcript player).

Usage: python3 tools/make-podcast.py [episode numbers…]
"""
import json, os, sys, re, wave, subprocess
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import podcast as P

KOKORO = Path(os.environ.get("KOKORO", ROOT.parent / "tts" / "kokoro-en-v0_19"))
OUT = ROOT / "podcast"; OUT.mkdir(exist_ok=True)
SR = 24000
VOICE = {"M": 6, "E": 1}          # am_michael, af_bella
SPEED = {"M": 1.0, "E": 1.02}

# what the synthesizer should say for things that are written one way and read another
SAY = [
    (r"\bELPA21\b", "ELPA twenty-one"), (r"\bELPT\b", "E L P T"), (r"\bEL\b", "E L"),
    (r"\bLSP\b", "L S P"), (r"\bIEP\b", "I E P"), (r"\bU\.?S\.?\b", "U S"),
    (r"radan55 dot github dot io slash everyteacher", "radan fifty-five dot github dot I O slash every teacher"),
    (r"\bninth-grade\b", "ninth grade"), (r"—", ", "), (r"\bnúcleo\b", "nucleo"), (r"\bmembrana\b", "membrana"),
]

def say(text):
    for a, b in SAY:
        text = re.sub(a, b, text)
    return text

def tts():
    import sherpa_onnx
    cfg = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(
            model=str(KOKORO / "model.onnx"), voices=str(KOKORO / "voices.bin"),
            tokens=str(KOKORO / "tokens.txt"), data_dir=str(KOKORO / "espeak-ng-data")),
        num_threads=2))
    return sherpa_onnx.OfflineTts(cfg)

def sting(sec=7.0, out=False):
    """A short musical sting in the house key (D), same family as the spot's bed."""
    n = int(sec * SR); t = np.arange(n) / SR; y = np.zeros(n)
    f = lambda m: 440 * 2 ** ((m - 69) / 12)
    chord = [50, 57, 61, 64, 69] if not out else [43, 50, 55, 57, 62]
    for i, m in enumerate(chord):
        for det in (-.002, 0, .002):
            y += (.2 if i == 0 else .11) * np.sin(2 * np.pi * f(m) * (1 + det) * t)
    env = np.ones(n); a = int(1.2 * SR); r = int(2.2 * SR)
    env[:a] = np.linspace(0, 1, a) ** 1.4; env[-r:] *= np.linspace(1, 0, r) ** 1.3
    y *= env
    for k, m in enumerate([62, 66, 69, 74] if not out else [74, 69, 66, 62]):
        s = int((0.6 + k * 0.42) * SR); nn = int(1.8 * SR); tt = t[:nn]
        y[s:s + nn] += .12 * (np.sin(2 * np.pi * f(m) * tt) + .3 * np.sin(4 * np.pi * f(m) * tt)) * np.exp(-tt * 2.6)
    return np.tanh(y * 1.2) * .5

def write_wav(path, x):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())

def main(nums):
    engine = tts()
    for ep in P.EPISODES:
        if nums and ep["n"] not in nums:
            continue
        print(f"episode {ep['n']}: {ep['title']}", flush=True)
        parts, cues, pos = [], [], 0.0
        intro = sting(); parts.append(intro); pos += len(intro) / SR - 2.6   # voice starts over the tail
        parts[-1] = intro
        gap_same, gap_switch = int(0.35 * SR), int(0.55 * SR)
        last = None
        for i, (who, text) in enumerate(ep["turns"]):
            a = engine.generate(say(text), sid=VOICE[who], speed=SPEED[who])
            x = np.array(a.samples, dtype=np.float32)
            # trim silence at the ends
            idx = np.where(np.abs(x) > 0.01)[0]
            if len(idx): x = x[max(0, idx[0] - int(.05 * SR)): idx[-1] + int(.12 * SR)]
            gap = 0 if last is None else (gap_switch if who != last else gap_same)
            if i == 0:
                # overlap the first line onto the intro tail
                start = len(intro) - int(2.6 * SR)
                buf = np.concatenate([intro, np.zeros(max(0, start + len(x) - len(intro)))])
                buf[start:start + len(x)] += x
                parts = [buf]; pos = start / SR
            else:
                parts.append(np.zeros(gap)); pos = sum(len(p) for p in parts) / SR
                parts.append(x)
            cues.append({"who": who, "t": round(pos, 2), "text": text})
            last = who
            print(f"  {i+1:2d}/{len(ep['turns'])} {who} {len(x)/SR:5.1f}s", flush=True)
        outro = sting(out=True)
        parts.append(np.zeros(int(.8 * SR))); parts.append(outro)
        y = np.concatenate(parts)
        # gentle level: speech peaks ~ -3 dB
        y = y / max(1e-6, np.percentile(np.abs(y), 99.9)) * 0.7
        wav = OUT / f"ep-{ep['n']}.wav"; write_wav(wav, y)
        mp3 = OUT / f"ep-{ep['n']}.mp3"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav),
                        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100", "-ac", "1",
                        "-c:a", "libmp3lame", "-b:a", "80k", "-id3v2_version", "3",
                        "-metadata", f"title=Ep. {ep['n']} · {ep['title']}",
                        "-metadata", "artist=EL Publishing", "-metadata", "album=Every Teacher",
                        "-metadata", f"track={ep['n']}", str(mp3)], check=True)
        wav.unlink()
        dur = len(y) / SR
        (OUT / f"ep-{ep['n']}.json").write_text(json.dumps(
            {"n": ep["n"], "title": ep["title"], "desc": ep["desc"], "duration": round(dur, 1),
             "bytes": mp3.stat().st_size, "cues": cues}, ensure_ascii=False, indent=1))
        print(f"  -> {mp3.name} {dur/60:.1f} min, {mp3.stat().st_size//1024} KB", flush=True)

if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]])
