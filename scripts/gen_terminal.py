W,H=900,260
F="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
cmd="./projects --status"
rows=[
 ("egg-farm","UP","egg-farm.aydexis.com"),
 ("menuor","UP","multi-tenant menus · auto-TLS per domain"),
 ("aydexCloud","UP","go tracker · next.js dashboard"),
 ("futsal","UP","role-based court booking"),
 ("fintrack","UP","SMS → categorized spend"),
]
cw=8.1
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{F}" font-size="13">',
'<title>Terminal: projects status</title>',
'<style>',
'.l{opacity:0;animation:in .01s forwards}',
'@keyframes in{to{opacity:1}}',
'.k{fill:#38f2c8}.d{fill:#6f86b3}.w{fill:#d7e5ff}.ok{fill:#38f2c8;font-weight:700}',
'.cur{fill:#38f2c8;animation:b 1s steps(1) infinite}',
'@keyframes b{50%{opacity:0}}',
'</style>',
f'<defs><clipPath id="tc"><rect x="0" y="0" width="0" height="30"><animate attributeName="width" from="0" to="{len(cmd)*cw:.0f}" dur="1.4s" begin="0.6s" fill="freeze" calcMode="discrete" values="{";".join(str(round(i*cw)) for i in range(len(cmd)+1))}"/></rect></clipPath></defs>',
f'<rect width="{W}" height="{H}" rx="12" fill="#04070d"/><rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#1d2f55"/>',
'<circle cx="22" cy="20" r="5" fill="#ff5f57"/><circle cx="40" cy="20" r="5" fill="#febc2e"/><circle cx="58" cy="20" r="5" fill="#28c840"/>',
f'<text x="{W/2}" y="24" text-anchor="middle" class="d" font-size="11">ayush@node-01: ~</text>',
'<text x="24" y="62"><tspan class="k">ayush@node-01</tspan><tspan class="d">:~$</tspan></text>']
px=24+ (len("ayush@node-01:~$ ")*cw)
o.append(f'<g transform="translate({px:.0f},0)"><g clip-path="url(#tc)"><text x="0" y="62" class="w">{cmd}</text></g></g>')
t0=2.2
for i,(n,s,desc) in enumerate(rows):
    y=92+i*24
    o.append(f'<g class="l" style="animation-delay:{t0+i*0.35:.2f}s"><text x="24" y="{y}" xml:space="preserve"><tspan class="w">{n:<12}</tspan><tspan class="d">[ </tspan><tspan class="ok">{s}</tspan><tspan class="d"> ]</tspan><tspan class="d">  {desc}</tspan></text></g>')
yy=92+len(rows)*24+8
o.append(f'<g class="l" style="animation-delay:{t0+len(rows)*0.35+0.3:.2f}s"><text x="24" y="{yy}" class="d">5 services up · 0 degraded · last deploy: today</text></g>')
o.append(f'<g class="l" style="animation-delay:{t0+len(rows)*0.35+0.8:.2f}s"><text x="24" y="{yy+30}"><tspan class="k">ayush@node-01</tspan><tspan class="d">:~$ </tspan></text><rect class="cur" x="{24+17*cw:.0f}" y="{yy+18}" width="8" height="15"/></g>')
o.append('</svg>')
open('assets/terminal.svg','w').write('\n'.join(o))
