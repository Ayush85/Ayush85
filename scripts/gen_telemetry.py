import json, os, sys, urllib.request, datetime as dt
LOGIN = os.environ.get("PROFILE_LOGIN", "Ayush85")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
F = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

def api(url, data=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-telemetry")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def load():
    if len(sys.argv) > 1:
        return json.load(open(sys.argv[1]))
    q = {"query": 'query($l:String!){user(login:$l){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{contributionCount}}}}}}', "variables": {"l": LOGIN}}
    cal = api("https://api.github.com/graphql", q)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in cal["weeks"]]
    repos = api(f"https://api.github.com/users/{LOGIN}/repos?per_page=100&sort=pushed&type=owner")
    return {"weeks": weeks, "total": cal["totalContributions"],
            "repos": [{"name": r["name"], "language": r["language"], "pushed_at": r["pushed_at"], "fork": r["fork"]} for r in repos]}

def render(d, now):
    weeks = d["weeks"][-26:]
    mx = max(weeks) or 1
    repos = [r for r in d["repos"] if not r["fork"]]
    langs = {}
    for r in repos:
        if r["language"]:
            langs[r["language"]] = langs.get(r["language"], 0) + 1
    top = sorted(langs.items(), key=lambda x: -x[1])[:6]
    tl = sum(v for _, v in top) or 1
    recent = sorted(repos, key=lambda r: r["pushed_at"], reverse=True)[:5]
    W, H = 900, 250
    pal = ["#38f2c8", "#7aa2ff", "#c792ff", "#ffb86b", "#ff7ab8", "#9aa7c7"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{F}">',
         '<title>GitHub telemetry</title>',
         '<style>.d{fill:#6f86b3;font-size:10px}.w{fill:#d7e5ff;font-size:12px}.h{fill:#38f2c8;font-size:11px;font-weight:700;letter-spacing:1px}.bar{transform-origin:bottom;animation:g .9s ease-out both}@keyframes g{from{transform:scaleY(0)}}</style>',
         f'<rect width="{W}" height="{H}" rx="12" fill="#070b14"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#1d2f55"/>',
         '<text class="h" x="24" y="30">COMMIT ACTIVITY · LAST 26 WEEKS</text>']
    bw = 14
    for i, v in enumerate(weeks):
        h = max(2, round(v / mx * 110))
        x = 24 + i * (bw + 4)
        o.append(f'<rect class="bar" style="animation-delay:{i*0.03:.2f}s" x="{x}" y="{175-h}" width="{bw}" height="{h}" rx="2" fill="#38f2c8" fill-opacity="{0.35+0.65*v/mx:.2f}"/>')
    o.append(f'<text class="d" x="24" y="196">{d["total"]} contributions in the last year · peak week {mx}</text>')
    x0 = 520
    o.append(f'<text class="h" x="{x0}" y="30">LANGUAGE MIX (OWNED REPOS)</text>')
    cx = x0
    for i, (n, v) in enumerate(top):
        w = round(v / tl * 356)
        o.append(f'<rect x="{cx}" y="42" width="{max(w,3)}" height="10" rx="2" fill="{pal[i]}"/>')
        o.append(f'<text class="w" x="{x0}" y="{74+i*16}"><tspan fill="{pal[i]}">■</tspan> {n} <tspan class="d">{round(v/tl*100)}%</tspan></text>')
        cx += w + 2
    o.append(f'<text class="h" x="{x0}" y="178">RECENT PUSHES</text>')
    for i, r in enumerate(recent[:3]):
        days = (now - dt.datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00"))).days
        ago = "today" if days == 0 else f"{days}d ago"
        o.append(f'<text class="w" x="{x0}" y="{198+i*16}">{r["name"]} <tspan class="d">{ago}</tspan></text>')
    o.append(f'<text class="d" x="24" y="{H-12}">generated {now:%Y-%m-%d %H:%M} UTC from the GitHub API</text>')
    o.append('</svg>')
    return "\n".join(o)

if __name__ == "__main__":
    now = dt.datetime.now(dt.timezone.utc)
    svg = render(load(), now)
    open("assets/telemetry.svg", "w").write(svg)
