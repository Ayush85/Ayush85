import os, random, sys
from common import *

PATH = "data/game.json"
SERVICES = ["api", "db", "cache", "queue"]
MOVES = {
    "restart api": {"api": 35},
    "restart db": {"db": 35},
    "restart cache": {"cache": 35},
    "restart queue": {"queue": 35},
    "scale api": {"api": 15, "db": -5},
    "failover db": {"db": 40, "cache": -10},
    "flush cache": {"cache": 40, "api": -10},
    "drain queue": {"queue": 40, "db": -5},
}
WIN, HIT = 70, 15

def new_round(n):
    rng = random.Random(1000 + n)
    return {s: rng.randint(35, 60) for s in SERVICES}

def fresh():
    return {"round": 1, "services": new_round(1), "moves": [], "last_login": "", "wins": 0, "outages": 0, "history": []}

def clamp(v):
    return max(0, min(100, v))

def play(state, login, cmd, seed):
    if cmd not in MOVES:
        return "Unknown command, nothing changed."
    if login == state["last_login"]:
        return "Another player has to take the next turn."
    sv = state["services"]
    for s, d in MOVES[cmd].items():
        sv[s] = clamp(sv[s] + d)
    hit = random.Random(seed).choice(SERVICES)
    sv[hit] = clamp(sv[hit] - HIT)
    state["moves"].append({"login": login, "cmd": cmd, "hit": hit})
    state["moves"] = state["moves"][-8:]
    state["last_login"] = login
    outcome = None
    if all(v >= WIN for v in sv.values()):
        outcome = "RESOLVED"
        state["wins"] += 1
    elif any(v == 0 for v in sv.values()):
        outcome = "OUTAGE"
        state["outages"] += 1
    msg = f"{cmd} applied. Incident hit {hit} (-{HIT})."
    if outcome:
        state["history"] = (state["history"] + [{"round": state["round"], "result": outcome, "by": login}])[-5:]
        state["round"] += 1
        state["services"] = new_round(state["round"])
        state["last_login"] = ""
        msg += f" Round ended: {outcome}. Round {state['round']} begins."
    return msg

def render(st):
    out = []
    out.append(f'<text x="24" y="52" class="k">incident-response</text><text x="{24+17*8.1:.0f}" y="52" class="d">  round {st["round"]} · resolved {st["wins"]} · outages {st["outages"]}</text>')
    y = 82
    for s in SERVICES:
        v = st["services"][s]
        col = "k" if v >= WIN else ("y" if v >= 35 else "r")
        fill = {"k": "#38f2c8", "y": "#ffcc66", "r": "#ff7a90"}[col]
        out.append(f'<text x="24" y="{y}" class="w">{s:<7}</text>')
        out.append(f'<rect x="100" y="{y-11}" width="300" height="12" rx="3" fill="#0f1a30"/><rect x="100" y="{y-11}" width="{3*v}" height="12" rx="3" fill="{fill}"/>')
        out.append(f'<rect x="{100+3*WIN-1}" y="{y-14}" width="2" height="18" fill="#6f86b3"/>')
        out.append(f'<text x="412" y="{y}" class="{col}">{v:>3}%</text>')
        y += 26
    out.append(f'<text x="24" y="{y+10}" class="d">goal: every service at or above {WIN}%.</text><text x="24" y="{y+28}" class="d">each turn the incident hits a random service for -{HIT}. a service at 0% is an outage.</text>')
    y += 18
    out.append('<text x="500" y="52" class="d">recent turns</text>')
    my = 76
    for m in reversed(st["moves"][-6:]):
        out.append(f'<text x="500" y="{my}" xml:space="preserve"><tspan class="k">{escape(m["login"])}</tspan><tspan class="d"> ran </tspan><tspan class="w">{escape(m["cmd"])}</tspan><tspan class="d"> · {escape(m["hit"])} hit</tspan></text>')
        my += 18
    if not st["moves"]:
        out.append('<text x="500" y="76" class="d">no turns yet. take the first one.</text>')
    if st["history"]:
        h = st["history"][-1]
        cls = "k" if h["result"] == "RESOLVED" else "r"
        out.append(f'<text x="24" y="{y+34}" class="{cls}">last round: {h["result"]} (final move by {escape(h["by"])})</text>')
    out.append(f'<text x="24" y="{y+58}" class="k">visitor@ayush85</text><text x="{24+15*8.1:.0f}" y="{y+58}" class="d">:~$ open an issue to move</text><rect class="cur" x="{24+36*8.1:.0f}" y="{y+46}" width="8" height="15"/>')
    return frame(900, y + 80, "incident-response.sh", "\n".join(out))

def main():
    ev = event()
    issue = ev["issue"]
    login = clean_login(issue["user"]["login"])
    st = load_json(PATH, None) or fresh()
    cmd = clean_text(form_field(issue.get("body"), "Command"), 30)
    if not login:
        reply = "Could not read a valid GitHub login, nothing changed."
    else:
        reply = play(st, login, cmd, int(issue["number"]))
        save_json(PATH, st)
    os.makedirs("assets", exist_ok=True)
    open("assets/game.svg", "w").write(render(st))
    open(os.environ.get("REPLY_FILE", "/tmp/reply.txt"), "w").write(reply + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "render":
        st = load_json(PATH, None) or fresh()
        save_json(PATH, st)
        os.makedirs("assets", exist_ok=True)
        open("assets/game.svg", "w").write(render(st))
    else:
        main()
