import json, re, sys

path = sys.argv[1]
d = json.load(open(path, encoding='utf-8'))
pages = d.get('query', {}).get('pages', {})
for pid, p in pages.items():
    t = p.get('title', '?')
    ii = (p.get('imageinfo') or [{}])[0]
    meta = ii.get('extmetadata', {})
    lic = meta.get('LicenseShortName', {}).get('value', '?')
    date = meta.get('DateOriginal', {}).get('value', meta.get('Date', {}).get('value', '?'))
    date = re.sub('<[^>]+>', '', date)[:60]
    print(t, '|', lic, '|', date, '|', ii.get('url', ''))
