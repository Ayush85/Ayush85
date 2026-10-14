import json, os, re
from xml.sax.saxutils import escape

FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
LOGIN_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
MSG_BAD = re.compile(r"[^A-Za-z0-9 .,!?'\-_:()+/]")

def load_json(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=1, sort_keys=True)
        f.write("\n")

def clean_login(value):
    value = str(value or "")
    return value if LOGIN_RE.match(value) else None

def clean_text(value, limit):
    value = MSG_BAD.sub("", str(value or ""))
    value = re.sub(r"\s+", " ", value).strip()
    return value[:limit]

def form_field(body, heading):
    m = re.search(r"###\s*" + re.escape(heading) + r"\s*\n+(.*?)(?:\n###|\Z)", body or "", re.S)
    return m.group(1).strip() if m else ""

def event():
    with open(os.environ["GITHUB_EVENT_PATH"]) as f:
        return json.load(f)

def frame(w, h, title, body, extra_css=""):
    esc = escape(title)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}" font-size="13">\n'
            f'<title>{esc}</title>\n<style>.d{{fill:#6f86b3}}.w{{fill:#d7e5ff}}.k{{fill:#38f2c8}}.r{{fill:#ff7a90}}.y{{fill:#ffcc66}}'
            f'.cur{{fill:#38f2c8;animation:b 1s steps(1) infinite}}@keyframes b{{50%{{opacity:0}}}}{extra_css}</style>\n'
            f'<rect width="{w}" height="{h}" rx="12" fill="#04070d"/><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="none" stroke="#1d2f55"/>\n'
            '<circle cx="22" cy="20" r="5" fill="#ff5f57"/><circle cx="40" cy="20" r="5" fill="#febc2e"/><circle cx="58" cy="20" r="5" fill="#28c840"/>\n'
            f'<text x="{w/2}" y="24" text-anchor="middle" class="d" font-size="11">{esc}</text>\n'
            f'{body}\n</svg>\n')
