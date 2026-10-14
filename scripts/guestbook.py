import datetime as dt, os, sys
from common import *

KEEP = 14
PATH = "data/guestbook.json"

def render(entries):
    rows = []
    y = 62
    for e in entries[-KEEP:]:
        rows.append(f'<text x="24" y="{y}" xml:space="preserve"><tspan class="d">[{escape(e["date"])}]</tspan> <tspan class="k">{escape(e["login"])}</tspan><tspan class="d">@visitor</tspan> <tspan class="w">&gt; {escape(e["msg"])}</tspan></text>')
        y += 20
    if not entries:
        rows.append('<text x="24" y="62" class="d">no entries yet. be the first to sign.</text>')
        y = 82
    rows.append(f'<text x="24" y="{y+14}" class="k">visitor@ayush85</text><text x="{24+15*8.1:.0f}" y="{y+14}" class="d">:~$ </text><rect class="cur" x="{24+19*8.1:.0f}" y="{y+2}" width="8" height="15"/>')
    h = max(150, y + 36)
    return frame(900, h, "guestbook.log", "\n".join(rows))

def main():
    ev = event()
    issue = ev["issue"]
    login = clean_login(issue["user"]["login"])
    entries = load_json(PATH, [])
    msg = clean_text(form_field(issue.get("body"), "Message"), 60)
    reply = ""
    if not login:
        reply = "Could not read a valid GitHub login, nothing was added."
    else:
        msg = msg or "was here"
        entries = [e for e in entries if e["login"] != login]
        entries.append({"login": login, "msg": msg, "date": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M")})
        entries = entries[-KEEP:]
        save_json(PATH, entries)
        reply = f"Thanks {login}, your line was added to the guestbook."
    os.makedirs("assets", exist_ok=True)
    open("assets/guestbook.svg", "w").write(render(entries))
    open(os.environ.get("REPLY_FILE", "/tmp/reply.txt"), "w").write(reply + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "render":
        os.makedirs("assets", exist_ok=True)
        open("assets/guestbook.svg", "w").write(render(load_json(PATH, [])))
    else:
        main()
