#!/usr/bin/env python3
"""Build the avatar PD session: video/session.json (+wav) then video/session.mp4.

  python3 tools/make-session.py audio
  python3 tools/make-session.py render
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import session as S
mp = __import__("make-podcast")
mv = __import__("make-videos")
SR = mp.SR; OUT = ROOT / "video"; FPS = 24; GAP = 0.5

def audio(_):
    engine = mp.tts()
    parts, beats, pos = [np.zeros(int(0.8 * SR))], [], 0.8
    for b in S.BEATS:
        kind, args, say = b[0], list(b[1:-1]), b[-1]
        a = engine.generate(mp.say(say), sid=S.VOICE, speed=1.0)
        x = np.array(a.samples, dtype=np.float32)
        idx = np.where(np.abs(x) > 0.01)[0]
        if len(idx): x = x[max(0, idx[0] - int(.05 * SR)): idx[-1] + int(.1 * SR)]
        d = len(x) / SR
        beats.append({"type": kind, "a": args, "t": round(pos, 3), "say": say, "chunks": mv.chunks_for(say, pos, d)})
        parts += [x, np.zeros(int(GAP * SR))]; pos += d + GAP
        print(f"  {kind:6s} {d:5.1f}s  total {pos/60:.1f} min", flush=True)
    pos += 1.8; parts.append(np.zeros(int(1.8 * SR)))
    voice = np.concatenate(parts)
    # loudness envelope at FPS for the mouth, from the voice alone
    hop = SR // FPS; n = len(voice) // hop
    env = np.array([np.sqrt(np.mean(voice[i*hop:(i+1)*hop] ** 2)) for i in range(n)])
    env = env / max(1e-6, np.percentile(env, 97)); env = np.clip(env, 0, 1)
    env = np.convolve(env, [0.25, 0.5, 0.25], mode="same")
    # soft pad
    n2 = len(voice); t = np.arange(n2) / SR; pad = np.zeros(n2); f = lambda m: 440 * 2 ** ((m - 69) / 12)
    for i, m in enumerate([38, 50, 57, 61]): pad += (.12 if i == 0 else .06) * np.sin(2 * np.pi * f(m) * t) * (1 + .15 * np.sin(2 * np.pi * .07 * t + i))
    e = np.ones(n2); a_ = int(2 * SR); r_ = int(3 * SR); e[:a_] = np.linspace(0, 1, a_); e[-r_:] *= np.linspace(1, 0, r_)
    mix = voice * 0.95 + pad * e * 0.13
    mix = mix / max(1e-6, np.percentile(np.abs(mix), 99.9)) * 0.75
    mp.write_wav(OUT / "session.wav", mix)
    (OUT / "session.json").write_text(json.dumps({"title": S.TITLE, "sub": S.SUB, "presenter": S.PRESENTER, "total": round(pos, 3), "fps": FPS,
                                                  "beats": beats, "env": [round(float(v), 3) for v in env]}, ensure_ascii=False))
    # captions
    def ts(s): return f"{int(s//3600):02d}:{int(s%3600//60):02d}:{s%60:06.3f}"
    out, k = ["WEBVTT", ""], 1
    for b in beats:
        for c in b["chunks"]: out += [str(k), f"{ts(c['t'])} --> {ts(c['e'])}", c["text"], ""]; k += 1
    (OUT / "session.vtt").write_text("\n".join(out))
    print(f"-> {pos/60:.1f} min, {len(beats)} beats", flush=True)

def render(_):
    js = Path("/tmp/claude-0/-home-claude/8b8003a1-aa3b-52bd-bcbf-19614c79fc15/scratchpad/render-session.mjs")
    js.write_text(mv.RENDER_JS.replace("video-stage.html?v='+n+'&render", "avatar-stage.html?render"))
    fr = Path("/tmp/claude-0/-home-claude/8b8003a1-aa3b-52bd-bcbf-19614c79fc15/scratchpad/fr-session"); fr.mkdir(exist_ok=True)
    for f in fr.glob("*.jpg"): f.unlink()
    subprocess.run(["node", str(js), "0", str(FPS), str(fr)], check=True, cwd="/home/claude")
    mp4 = OUT / "session.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(fr / "%05d.jpg"), "-i", str(OUT / "session.wav"),
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "128k", "-shortest",
                    "-metadata", f"title=The session · {S.TITLE}", "-metadata", "artist=EL Publishing", str(mp4)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "6", "-i", str(mp4), "-frames:v", "1", "-q:v", "3", str(OUT / "session-poster.jpg")], check=True)
    for f in fr.glob("*.jpg"): f.unlink()
    print(f"-> {mp4.name} {mp4.stat().st_size//1024//1024} MB")

if __name__ == "__main__":
    {"audio": audio, "render": render}[sys.argv[1] if len(sys.argv) > 1 else "audio"](None)
