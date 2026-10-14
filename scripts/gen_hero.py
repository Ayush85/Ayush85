W,H=900,330
F="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
nodes={
 'users':(30,175,90,46,'users','HTTPS'),
 'nginx':(160,175,100,46,'nginx','JWT / NJS'),
 'ha':(300,175,110,46,'HAProxy','active-active'),
 'ka':(470,115,120,46,'k3s node A','workloads'),
 'kb':(470,235,120,46,'k3s node B','workloads'),
 'my':(670,85,150,46,'MySQL 8.4','GTID semi-sync'),
 'mq':(670,170,150,46,'MQTT bus','access sync'),
 'ob':(670,255,150,46,'Observability','prom · grafana · loki'),
}
def c(n,side):
    x,y,w,h,_,_=nodes[n]
    return (x+w if side=='r' else x, y+h/2)
edges=[('users','nginx'),('nginx','ha'),('ha','ka'),('ha','kb'),('ka','my'),('ka','mq'),('kb','mq'),('kb','ob')]
o=[]
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{F}">')
o.append('<title>Ayush Shrestha: production platform topology</title>')
o.append('''<defs>
<pattern id="g" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="#12203a" stroke-width="1"/></pattern>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050912"/><stop offset="1" stop-color="#0a1426"/></linearGradient>
<linearGradient id="sc" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#38f2c8" stop-opacity="0"/><stop offset=".5" stop-color="#38f2c8" stop-opacity=".07"/><stop offset="1" stop-color="#38f2c8" stop-opacity="0"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<style>
.n{fill:#0b1426;stroke:#2a4a86;stroke-width:1.2}
.t{fill:#d7e5ff;font-size:13px;font-weight:700}
.s{fill:#6f86b3;font-size:10px}
.e{stroke:#27406f;stroke-width:1.4;fill:none}
.led{fill:#38f2c8;animation:p 2.2s ease-in-out infinite}
@keyframes p{50%{opacity:.25}}
.scan{animation:sc 6s linear infinite}
@keyframes sc{from{transform:translateY(-80px)}to{transform:translateY(420px)}}
</style>''')
o.append(f'<rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/><rect width="{W}" height="{H}" rx="14" fill="url(#g)"/>')
o.append(f'<rect class="scan" width="{W}" height="80" fill="url(#sc)"/>')
o.append(f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#1d2f55"/>')
o.append(f'<text x="32" y="50" fill="#38f2c8" font-size="30" font-weight="800" letter-spacing="3" filter="url(#glow)">AYUSH SHRESTHA</text>')
o.append(f'<text x="32" y="74" fill="#8fb3ff" font-size="13">full-stack · infrastructure · distributed systems</text>')
o.append(f'<text x="{W-32}" y="46" fill="#6f86b3" font-size="11" text-anchor="end">node-01 · Kathmandu, NP</text>')
o.append(f'<text x="{W-32}" y="64" fill="#38f2c8" font-size="11" text-anchor="end"><tspan class="led">●</tspan> all systems nominal</text>')
for i,(a,b) in enumerate(edges):
    x1,y1=c(a,'r'); x2,y2=c(b,'l'); mx=(x1+x2)/2
    d=f'M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}'
    o.append(f'<path id="e{i}" class="e" d="{d}"/>')
for i,(a,b) in enumerate(edges):
    for k in range(2):
        dur=2.6+0.3*(i%3); begin=-(k*dur/2+0.2*i)
        o.append(f'<circle r="2.6" fill="#38f2c8" filter="url(#glow)"><animateMotion dur="{dur:.1f}s" begin="{begin:.2f}s" repeatCount="indefinite"><mpath href="#e{i}"/></animateMotion></circle>')
for k,(x,y,w,h,t,s) in nodes.items():
    o.append(f'<rect class="n" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>')
    o.append(f'<circle class="led" cx="{x+12}" cy="{y+14}" r="3" style="animation-delay:{(sum(map(ord,k))%10)/10:.1f}s"/>')
    o.append(f'<text class="t" x="{x+22}" y="{y+18}">{t}</text><text class="s" x="{x+12}" y="{y+35}">{s}</text>')
o.append(f'<text x="32" y="{H-18}" fill="#4d6592" font-size="10">$ platform --topology   # k3s · Proxmox · LXD · MySQL replication · MQTT</text>')
o.append('</svg>')
open('assets/hero.svg','w').write('\n'.join(o))
