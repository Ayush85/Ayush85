import datetime as dt, hashlib, math, os, sys
from common import *

PATH = "data/network.json"
LOGIN = os.environ.get("PROFILE_LOGIN", "Ayush85")
EXCLUDE = ("fatafat", "optix")

def fetch():
    import json, urllib.request
    q = {"query": 'query($l:String!){user(login:$l){contributionsCollection{contributionCalendar{weeks{contributionDays{date contributionCount}}} commitContributionsByRepository(maxRepositories:25){repository{name isPrivate} contributions{totalCount}}}}}', "variables": {"l": LOGIN}}
    req = urllib.request.Request("https://api.github.com/graphql", json.dumps(q).encode())
    req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    req.add_header("User-Agent", "profile-network")
    with urllib.request.urlopen(req, timeout=30) as r:
        cc = json.load(r)["data"]["user"]["contributionsCollection"]
    days = {d["date"]: d["contributionCount"] for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]}
    repos = [{"name": ("private-" + hashlib.sha1(x["repository"]["name"].encode()).hexdigest()[:4]) if x["repository"]["isPrivate"] else x["repository"]["name"], "n": x["contributions"]["totalCount"]} for x in cc["commitContributionsByRepository"]]
    return {"days": days, "repos": repos}

def h(*parts):
    return int(hashlib.sha1("|".join(map(str, parts)).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF

def merge(state, data):
    repos = [r for r in data["repos"] if not any(x in r["name"].lower() for x in EXCLUDE)]
    state["repos"] = repos or state.get("repos", [])
    seen = {n["date"] for n in state.get("nodes", [])}
    nodes = state.setdefault("nodes", [])
    names = [r["name"] for r in state["repos"]] or ["core"]
    for date in sorted(data["days"]):
        c = data["days"][date]
        if c > 0 and date not in seen:
            nodes.append({"date": date, "n": c, "repo": names[int(h("repo", date) * len(names))]})
    state["nodes"] = sorted(nodes, key=lambda n: n["date"])[-400:]
    return state

def render(st):
    W, H = 900, 360
    cx, cy = W / 2, H / 2
    repos = st.get("repos", [])[:12]
    pos = {}
    for i, r in enumerate(repos):
        a = 2 * math.pi * i / max(1, len(repos)) + 0.4
        rad = 70 + 25 * h("r", r["name"])
        pos[r["name"]] = (cx + 3.4 * rad * math.cos(a), cy + 1.7 * rad * math.sin(a))
    o = []
    nodes = st.get("nodes", [])
    pts = []
    total = max(1, len(nodes))
    for i, n in enumerate(nodes):
        base = pos.get(n["repo"], (cx, cy))
        a = 2 * math.pi * h("a", n["date"])
        d = 18 + 150 * (i / total) * h("d", n["date"]) + 12
        x = min(W - 14, max(14, base[0] + 2.4 * d * math.cos(a) * 0.6))
        y = min(H - 30, max(36, base[1] + 1.2 * d * math.sin(a) * 0.6))
        pts.append((x, y, n, base))
    edges = []
    for x, y, n, base in pts:
        edges.append(f'<line x1="{base[0]:.1f}" y1="{base[1]:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="#1f4a6e" stroke-opacity=".55"/>')
    rn = list(pos.values())
    for i in range(len(rn)):
        j = (i + 1) % len(rn)
        if i != j:
            edges.append(f'<line x1="{rn[i][0]:.1f}" y1="{rn[i][1]:.1f}" x2="{rn[j][0]:.1f}" y2="{rn[j][1]:.1f}" stroke="#2c6aa8" stroke-opacity=".7"/>')
    dots = []
    mx = max([n["n"] for _, _, n, _ in pts] or [1])
    for i, (x, y, n, _) in enumerate(pts):
        r = 1.5 + 3.5 * n["n"] / mx
        col = "#38f2c8" if h("c", n["date"]) > 0.3 else "#7aa2ff"
        dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}" fill-opacity="{0.5 + 0.5 * n["n"] / mx:.2f}" style="animation:tw {2 + 3 * h("t", n["date"]):.1f}s ease-in-out {h("o", n["date"]) * 3:.1f}s infinite"/>')
    hubs = []
    for r in repos:
        x, y = pos[r["name"]]
        hubs.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#04070d" stroke="#ff2bd6" stroke-width="1.5"/><text x="{x+11:.1f}" y="{y+4:.1f}" font-size="10" fill="#c9a7ff">{escape(r["name"][:18])}</text>')
    since = nodes[0]["date"] if nodes else "-"
    body = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">'
            f'<title>Commit network</title><style>@keyframes tw{{50%{{opacity:.25}}}}</style>'
            f'<rect width="{W}" height="{H}" rx="12" fill="#04070d"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#1d2f55"/>'
            + "".join(edges) + "".join(dots) + "".join(hubs) +
            f'<text x="24" y="28" font-size="11" font-weight="700" letter-spacing="1" fill="#38f2c8">COMMIT NETWORK · {len(nodes)} ACTIVE DAYS SINCE {since}</text>'
            f'<text x="24" y="{H-14}" font-size="10" fill="#4d6592">each dot is a day with real commits, attached to a repo hub. the graph grows every night. private repo names are hashed.</text></svg>\n')
    return body

if __name__ == "__main__":
    state = load_json(PATH, {})
    if len(sys.argv) > 1:
        data = load_json(sys.argv[1], {})
    else:
        data = fetch()
    state = merge(state, data)
    save_json(PATH, state)
    os.makedirs("assets", exist_ok=True)
    open("assets/network.svg", "w").write(render(state))
