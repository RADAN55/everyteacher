#!/usr/bin/env python3
"""Pull the feeds in tools/feeds.txt, keep the last 30 days, sort into
'el' (English-learner pedagogy) and 'gen' (of interest to any teacher),
and write daily/feed.json for today-in-el.html. Fault-tolerant per feed."""
import json, re, sys, time, html, pathlib, datetime as dt, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "daily" / "feed.json"
KEEP_DAYS = 30
PER_SOURCE = 15   # newest N per source per run, so one busy outlet cannot swamp the page
UA = "Mozilla/5.0 (compatible; EL-Publishing-hub-feed/1.0; +https://radan55.github.io/everyteacher/)"
EL_WORDS = re.compile(r"\b(english[- ]learners?|english[- ]language[- ]learners?|\bELs?\b|\bELLs?\b|multilingual|bilingual|biliteracy|dual[- ]language|newcomers?|immigrant|refugee|\bESL\b|\bESOL\b|\bENL\b|\bEFL\b|\bTESOL\b|language acquisition|second language|translanguaging|\bWIDA\b|ELPA21|\bELPT\b|Title III|Spanish[- ]speaking|home language|heritage language|sheltered instruction|\bSIOP\b|academic language|academic vocabulary|language learners?|Lau v\.|Castañeda|Plyler)\b", re.I)

def strip(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

def when(e, ns):
    for tag in ("pubDate", "published", "updated", "{http://purl.org/dc/elements/1.1/}date"):
        for el in e.iter():
            if el.tag.endswith(tag) and (el.text or "").strip():
                t = el.text.strip()
                try:
                    return parsedate_to_datetime(t).astimezone(dt.timezone.utc)
                except Exception:
                    try:
                        return dt.datetime.fromisoformat(t.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
                    except Exception:
                        pass
    return None

def items_lenient(xml):
    """Regex fallback for feeds that are not well-formed XML."""
    t = xml.decode("utf-8", "ignore") if isinstance(xml, bytes) else xml
    out = []
    for m in re.finditer(r"<(item|entry)\b.*?</\1>", t, re.S | re.I):
        blk = m.group(0)
        g = lambda tag: (re.search(r"<%s\b[^>]*>(.*?)</%s>" % (tag, tag), blk, re.S | re.I) or [None, ""])[1]
        title = strip(re.sub(r"^\s*<!\[CDATA\[|\]\]>\s*$", "", g("title")))
        link = strip(re.sub(r"<!\[CDATA\[|\]\]>", "", g("link"))) or (re.search(r'<link[^>]*href="([^"]+)"', blk) or [None, ""])[1]
        desc = strip(re.sub(r"<!\[CDATA\[|\]\]>", "", g("description") or g("summary") or g("content")))
        d = None
        dm = re.search(r"<(pubDate|published|updated|dc:date)>(.*?)</\1>", blk, re.S | re.I)
        if dm:
            try: d = parsedate_to_datetime(dm.group(2).strip()).astimezone(dt.timezone.utc)
            except Exception:
                try: d = dt.datetime.fromisoformat(dm.group(2).strip().replace("Z", "+00:00")).astimezone(dt.timezone.utc)
                except Exception: pass
        out.append((title, link, desc, d))
    return out

def items_of(xml):
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        return items_lenient(xml)
    out = []
    # RSS 2.0
    for it in root.iter("item"):
        title = strip((it.findtext("title") or ""))
        link = (it.findtext("link") or "").strip()
        desc = strip(it.findtext("description") or "")
        out.append((title, link, desc, when(it, None)))
    # Atom
    A = "{http://www.w3.org/2005/Atom}"
    for it in root.iter(A + "entry"):
        title = strip(it.findtext(A + "title") or "")
        link = ""
        for l in it.findall(A + "link"):
            if l.get("rel") in (None, "alternate") and l.get("href"):
                link = l.get("href"); break
        desc = strip(it.findtext(A + "summary") or it.findtext(A + "content") or "")
        out.append((title, link, desc, when(it, None)))
    return out

def main():
    feeds = []
    for line in (ROOT / "tools" / "feeds.txt").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"): continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 3: feeds.append(parts)
    now = dt.datetime.now(dt.timezone.utc)
    cutoff = now - dt.timedelta(days=KEEP_DAYS)
    prev = {}
    if OUT.exists():
        try:
            for it in json.loads(OUT.read_text()).get("items", []): prev[it["link"]] = it
        except Exception: pass
    items, status = {}, []
    for name, url, bucket in feeds:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"})
            with urllib.request.urlopen(req, timeout=25) as r:
                xml = r.read()
            got = items_of(xml)
            got = sorted(got, key=lambda x: x[3] or now, reverse=True)[:PER_SOURCE]
            n = 0
            for title, link, desc, d in got:
                if not title or not link: continue
                if d is None: d = now
                if d < cutoff: continue
                text = f"{title} {desc}"
                b = "el" if (bucket == "el" or EL_WORDS.search(text)) else "gen"
                items[link] = {"title": title[:200], "link": link, "source": name, "date": d.date().isoformat(),
                               "summary": desc[:320], "bucket": b, "ms": bool(re.search(r"Mississippi", text, re.I))}
                n += 1
            status.append({"source": name, "ok": True, "items": n})
        except Exception as e:
            status.append({"source": name, "ok": False, "error": str(e)[:120]})
            # keep what we already had from this source
            for link, it in prev.items():
                if it.get("source") == name and it.get("date", "0000") >= cutoff.date().isoformat():
                    items.setdefault(link, it)
    # carry forward anything recent we had but didn't see again (feeds only show the newest N)
    for link, it in prev.items():
        if it.get("date", "0000") >= cutoff.date().isoformat():
            items.setdefault(link, it)
    arr = sorted(items.values(), key=lambda x: (x["date"], x["title"]), reverse=True)
    data = {"updated": now.isoformat(timespec="minutes"), "keep_days": KEEP_DAYS, "sources": status,
            "counts": {"el": sum(1 for i in arr if i["bucket"] == "el"), "gen": sum(1 for i in arr if i["bucket"] == "gen")},
            "items": arr}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=0) + "\n")
    ok = sum(1 for s in status if s["ok"])
    print(f"{len(arr)} items ({data['counts']['el']} EL, {data['counts']['gen']} general) from {ok}/{len(status)} feeds")
    for s in status:
        if not s["ok"]: print("  FAILED", s["source"], "-", s.get("error"))

if __name__ == "__main__":
    main()
