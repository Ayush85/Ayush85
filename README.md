<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:05010f,40:1b0a3c,100:00f5d4&text=AYUSH%20SHRESTHA&fontColor=00f5d4&fontSize=54&fontAlignY=38&animation=twinkling&stroke=ff2bd6&strokeWidth=1&desc=%3E_%20Full%20Stack%20%7C%20Infrastructure%20%7C%20Distributed%20Systems&descColor=ff7ae6&descSize=18&descAlignY=62" alt="Ayush Shrestha"/>

<p align="center">
  <a href="https://github.com/ayush85"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=18&pause=900&color=00F5D4&center=true&vCenter=true&width=720&lines=%3E+booting+ayush.os+...+OK;%24+kubectl+get+nodes+--all;%24+mysql+%3E+SHOW+REPLICA+STATUS%5CG;%24+mosquitto_sub+-t+%27access%2F%23%27;%24+shipping+React+%2B+TypeScript+to+prod;%3E+building+systems+from+code+to+cluster" alt="typing intro"/></a>
</p>

<p align="center">
  <a href="https://linkedin.com/in/ayushshrestha85"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:ayushshrestha8585@gmail.com"><img src="https://img.shields.io/badge/Email-00F5D4?style=flat-square&logo=gmail&logoColor=0f2027" alt="Email"/></a>
  <img src="https://img.shields.io/badge/Kathmandu-Nepal%20🇳🇵-203a43?style=flat-square" alt="Location"/>
  <img src="https://img.shields.io/badge/Experience-4%2B%20years-203a43?style=flat-square" alt="Experience"/>
</p>

---

```text
[  OK  ] Started k3s cluster ............. 2 nodes
[  OK  ] Started MySQL 8.4 ............... GTID semi-sync replica
[  OK  ] Started nginx + HAProxy ......... JWT/NJS routing, active-active
[  OK  ] Started MQTT bus ................ real-time access control sync
[  OK  ] Started observability ........... Prometheus / Grafana / Loki
[ .... ] Loading next project ............ ready for collaboration
```

## `~ $ whoami`

```yaml
name:        Ayush Shrestha
role:        Full Stack & Infrastructure Engineer
location:    Kathmandu, Nepal
education:   B.E. Computer Engineering, Tribhuwan University
currently:   Mentor Friends Pvt. Ltd.
focus:
  - Operating a self-managed multi-node production platform (k3s + Proxmox + LXD)
  - MySQL replication, nginx / HAProxy traffic routing, observability
  - Distributed access control and real-time sync over MQTT
stack:       [TypeScript, React, .NET Core, Node.js, Django, Go, Kubernetes]
```

## `~ $ cat architecture.mmd`

A simplified view of the platform I build and run day to day.

```mermaid
flowchart LR
    U([Users]) --> N[nginx<br/>JWT routing via NJS]
    N --> H{{HAProxy<br/>active-active}}
    H --> A[Primary server A]
    H --> B[Primary server B]
    A --> K[(k3s cluster<br/>2 nodes)]
    B --> K
    K --> M[(MySQL primary)]
    M -. GTID semi-sync .-> R[(MySQL replica)]
    K --> Q[[MQTT<br/>real-time sync]]
    K -.-> O[Prometheus · Grafana · Loki]
    A -.-> O
    B -.-> O
```

## `~ $ ls ./stack`

<p>
  <img src="https://skillicons.dev/icons?i=ts,js,py,cs,go,php,html,css&theme=dark" alt="Languages"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=react,nodejs,express,dotnet,django,jquery&theme=dark" alt="Frameworks"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=postgres,mysql,supabase,sqlite,mongodb&theme=dark" alt="Databases"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,nginx,prometheus,grafana,githubactions,gitlab,digitalocean,git&theme=dark" alt="Infrastructure"/>
</p>

**Also:** Proxmox · LXD · HAProxy · Traefik · WireGuard · Loki · Alloy · k6 · MQTT · Certbot/ACME · Swagger · Jira

## `~ $ git log --career`

```text
* Dec 2024 - now   Mentor Friends Pvt. Ltd.
|                  Full Stack / Infrastructure Developer
|                  k3s + Proxmox + LXD platform, MySQL 8.0 -> 8.4 replication (27GB),
|                  nginx from source with JWT/NJS routing, HAProxy, Prometheus/Grafana/Loki,
|                  k6 load tests, FreeSchemaAccessControl, in-house CI/CD
|
* Jun 2023 - Sep 2024  Urban Nepal Consulting Pvt. Ltd.
|                  Full Stack Developer
|                  Optix SaaS backend modules in Django + PostgreSQL, DigitalOcean Spaces
|
* Nov 2022 - Jun 2023  Logicseed
                   Junior Full Stack Developer / Web Dev Intern
                   HR system (Django), Core PHP + Supabase, Pandas/Selenium scraping
```

## `~ $ ls -l ./projects`

| Project | Visibility | Stack | Engineering notes |
| --- | --- | --- | --- |
| [**egg-farm**](https://egg-farm.aydexis.com) | `live` | `TypeScript` | Management platform for poultry and egg farm operations (source private) |
| [**menuor**](https://github.com/ayush85/MoodMenu) | `public` | `Next.js` `Prisma` `Docker` | Multi-tenant menus; per-restaurant custom domains with cron-driven nginx vhost + certbot provisioning |
| [**aydexCloud**](https://github.com/ayush85/aydexCloud) | `public` | `Go` `Next.js` `Prisma` `Caddy` | Privacy-first analytics: Go event tracker, Next.js dashboard, Sentry, Compose deploy |
| **futsal** | `private` | `React` `Express` `Prisma` `Postgres` | Role-based booking (customer / owner / admin); slot lock on approve auto-rejects competing requests |
| [**FinTrack**](https://github.com/ayush85/FinTrack) | `public` | `React Native` | On-device SMS parsing into categorized debit/credit summaries |

## `~ $ ./stats.sh`

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=ayush85&theme=synthwave&hide_border=true&bg_color=0d0221&include_all_commits=true&count_private=true&show_icons=true" alt="GitHub stats"/>
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ayush85&theme=synthwave&hide_border=true&bg_color=0d0221&layout=compact" alt="Top languages"/>
  <br/>
  <img width="95%" src="https://github-readme-activity-graph.vercel.app/graph?username=ayush85&bg_color=0d0221&color=00f5d4&line=ff2bd6&point=ffffff&area=true&area_color=ff2bd6&hide_border=true" alt="Contribution graph"/>
</p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:00f5d4,50:1b0a3c,100:05010f&section=footer&animation=twinkling" alt=""/>
