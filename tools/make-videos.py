#!/usr/bin/env python3
"""Build the Six Moves videos from tools/videos.py.

  python3 tools/make-videos.py audio [n…]    synthesize narration → video/moves-N.json + .wav
  python3 tools/make-videos.py render [n…]   render frames with Playwright → video/moves-N.mp4 + poster

Needs sherpa-onnx + the Kokoro model (see make-podcast.py), ffmpeg, node+playwright,
and a local server on :8898 serving the repo (RangeHTTPServer or http.server).
"""
import json, os, re, subprocess, sys, wave
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import videos as V
mp = __import__("make-podcast")          # reuse say(), tts(), sting(), write_wav, SR
SR = mp.SR
OUT = ROOT / "video"; OUT.mkdir(exist_ok=True)
FPS = 24
GAP = 0.45

def chunks_for(text, t0, dur):
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    groups, cur = [], ""
    for s in sents:
        if cur and len(cur) + len(s) > 105:
            groups.append(cur); cur = s
        else:
            cur = (cur + " " + s).strip()
    if cur: groups.append(cur)
    n = sum(len(g) for g in groups) or 1
    out, t = [], t0
    for g in groups:
        d = dur * len(g) / n
        out.append({"text": g, "t": round(t, 3), "e": round(t + d, 3)}); t += d
    return out

def audio(nums):
    engine = mp.tts()
    for vid in V.VIDEOS:
        if nums and vid["n"] not in nums: continue
        print(f"video {vid['n']}: {vid['title']}", flush=True)
        parts, beats, pos = [], [], 0.6
        parts.append(np.zeros(int(0.6 * SR)))
        for b in vid["beats"]:
            kind, args, say = b[0], list(b[1:-1]), b[-1]
            a = engine.generate(mp.say(say), sid=V.VOICE, speed=1.0)
            x = np.array(a.samples, dtype=np.float32)
            idx = np.where(np.abs(x) > 0.01)[0]
            if len(idx): x = x[max(0, idx[0] - int(.05 * SR)): idx[-1] + int(.1 * SR)]
            d = len(x) / SR
            beats.append({"type": kind, "a": args, "t": round(pos, 3), "say": say, "chunks": chunks_for(say, pos, d)})
            parts.append(x); parts.append(np.zeros(int(GAP * SR)))
            pos += d + GAP
            print(f"  {kind:6s} {d:5.1f}s", flush=True)
        pos += 1.6; parts.append(np.zeros(int(1.6 * SR)))
        voice = np.concatenate(parts)
        # a quiet pad under the whole thing: the sting's chord, looped and softened
        n = len(voice); t = np.arange(n) / SR; pad = np.zeros(n)
        f = lambda m: 440 * 2 ** ((m - 69) / 12)
        for i, m in enumerate([38, 50, 57, 61]):
            pad += (.12 if i == 0 else .06) * np.sin(2 * np.pi * f(m) * t) * (1 + .15 * np.sin(2 * np.pi * 0.07 * t + i))
        env = np.ones(n); a_ = int(2 * SR); r_ = int(3 * SR)
        env[:a_] = np.linspace(0, 1, a_); env[-r_:] *= np.linspace(1, 0, r_)
        pad *= env * 0.16
        mix = voice * 0.95 + pad
        mix = mix / max(1e-6, np.percentile(np.abs(mix), 99.9)) * 0.75
        mp.write_wav(OUT / f"moves-{vid['n']}.wav", mix)
        (OUT / f"moves-{vid['n']}.json").write_text(json.dumps(
            {"n": vid["n"], "title": vid["title"], "tag": V.TAG, "total": round(pos, 3), "beats": beats}, ensure_ascii=False))
        print(f"  -> {pos/60:.1f} min", flush=True)

RENDER_JS = r"""
import {chromium} from 'playwright'; import fs from 'fs';
const [n,fps,dir]=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto('http://127.0.0.1:8898/video-stage.html?v='+n+'&render',{waitUntil:'networkidle'});
await p.waitForFunction(()=>window.__spot);await p.evaluate(()=>window.__spot.ready);await p.waitForTimeout(500);
const T=await p.evaluate(()=>window.__spot.duration);const N=Math.ceil(T/1000*fps);
const cdp=await p.context().newCDPSession(p);const t0=Date.now();
for(let i=0;i<N;i++){await p.evaluate(t=>window.__spot.seek(t),Math.min(T,i*1000/fps));
  const {data}=await cdp.send('Page.captureScreenshot',{format:'jpeg',quality:90});
  fs.writeFileSync(dir+'/'+String(i).padStart(5,'0')+'.jpg',Buffer.from(data,'base64'));
  if(i%500===0)console.log(n,i,'/',N,((Date.now()-t0)/1000|0)+'s');}
await b.close();console.log('frames',N);
"""

def render(nums):
    js = Path("/tmp/claude-0/-home-claude/8b8003a1-aa3b-52bd-bcbf-19614c79fc15/scratchpad/render-moves.mjs")
    js.write_text(RENDER_JS)
    for vid in V.VIDEOS:
        n = vid["n"]
        if nums and n not in nums: continue
        wav = OUT / f"moves-{n}.wav"
        if not wav.exists(): print(f"no audio for {n}; run audio first"); continue
        fr = Path(f"/tmp/claude-0/-home-claude/8b8003a1-aa3b-52bd-bcbf-19614c79fc15/scratchpad/fr-moves-{n}")
        fr.mkdir(exist_ok=True)
        for f in fr.glob("*.jpg"): f.unlink()
        subprocess.run(["node", str(js), str(n), str(FPS), str(fr)], check=True, cwd="/home/claude")
        mp4 = OUT / f"moves-{n}.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(fr / "%05d.jpg"), "-i", str(wav),
                        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "128k", "-shortest",
                        "-metadata", f"title=Six Moves {n} · {vid['title']}", "-metadata", "artist=EL Publishing", str(mp4)], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "2.2", "-i", str(mp4), "-frames:v", "1", "-q:v", "3", str(OUT / f"moves-{n}-poster.jpg")], check=True)
        for f in fr.glob("*.jpg"): f.unlink()
        print(f"  -> {mp4.name} {mp4.stat().st_size//1024//1024} MB", flush=True)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "audio"
    nums = [int(a) for a in sys.argv[2:]]
    {"audio": audio, "render": render}[cmd](nums)
