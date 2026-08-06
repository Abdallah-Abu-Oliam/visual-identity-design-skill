import json
import re
import sys
import urllib.request
import urllib.parse
import os
import time

FORBIDDEN_TITLE_TAGS = [
    "radiation", "radioactive", "nuclear power plant", "cooling tower",
    "geiger", "dosimeter", "hazard", "biohazard", "trefoil",
    "reactor", "power plant", "hard hat", "protest", "placard",
    "warning sign", "toxic",
]

def fetch(query, page_size=20, page=1, license_type="commercial,modification"):
    base = "https://api.openverse.org/v1/images/"
    params = {
        "q": query,
        "page_size": str(page_size),
        "page": str(page),
        "mature": "false",
    }
    url = base + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research-agent"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("results", [])
    except Exception as e:
        print(f"ERROR fetching query='{query}': {e}", file=sys.stderr)
        return []

def is_forbidden(item):
    text = (item.get("title") or "").lower()
    tags = item.get("tags") or []
    tagtext = " ".join([t.get("name", "") for t in tags if isinstance(t, dict)]).lower()
    combined = text + " " + tagtext
    for bad in FORBIDDEN_TITLE_TAGS:
        if bad in combined:
            return True
    return False

def sanitize(s, maxlen=40):
    s = re.sub(r"[^a-zA-Z0-9\- ]", "", s or "")
    s = re.sub(r"\s+", "-", s.strip())
    return s[:maxlen].strip("-").lower()

def download(item, out_dir, prefix, index, log_lines):
    url = item.get("url")
    if not url:
        return False
    ext = os.path.splitext(urllib.parse.urlparse(url).path)[1]
    if not ext or len(ext) > 5:
        ext = ".jpg"
    title_slug = sanitize(item.get("title") or "untitled")
    fname = f"{prefix}-{title_slug}-{index:02d}{ext}"
    fpath = os.path.join(out_dir, fname)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research-agent"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
        if len(content) < 3000:
            print(f"SKIP too small: {url}", file=sys.stderr)
            return False
        with open(fpath, "wb") as f:
            f.write(content)
        log_lines.append(f"{fname}\t{url}\t{item.get('license')}\t{item.get('creator')}\t{item.get('foreign_landing_url')}\t{item.get('title')}")
        print(f"OK {fname}")
        return True
    except Exception as e:
        print(f"FAIL download {url}: {e}", file=sys.stderr)
        return False

def run(query, out_dir, prefix, want, log_path):
    os.makedirs(out_dir, exist_ok=True)
    collected = 0
    page = 1
    log_lines = []
    seen_urls = set()
    attempts = 0
    while collected < want and attempts < 6:
        results = fetch(query, page_size=20, page=page)
        attempts += 1
        if not results:
            break
        for item in results:
            if collected >= want:
                break
            url = item.get("url")
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)
            if is_forbidden(item):
                print(f"FILTERED (forbidden term): {item.get('title')}", file=sys.stderr)
                continue
            if download(item, out_dir, prefix, collected + 1, log_lines):
                collected += 1
            time.sleep(0.15)
        page += 1
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n## Query: {query}\nResults collected: {collected}\n")
        for line in log_lines:
            f.write(line + "\n")
    print(f"=== query '{query}' collected {collected}/{want} ===")
    return collected

if __name__ == "__main__":
    # args: query out_dir prefix want log_path
    query = sys.argv[1]
    out_dir = sys.argv[2]
    prefix = sys.argv[3]
    want = int(sys.argv[4])
    log_path = sys.argv[5]
    run(query, out_dir, prefix, want, log_path)
