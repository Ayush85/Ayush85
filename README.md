<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0f2027,50:203a43,100:2c5364&text=Ayush%20Shrestha&fontColor=00f5d4&fontSize=52&fontAlignY=38&desc=Full%20Stack%20and%20Infrastructure%20Engineer&descColor=9be7ff&descSize=18&descAlignY=60" alt="Ayush Shrestha"/>

<p align="center">
  <a href="https://github.com/ayush85"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1200&color=00F5D4&center=true&vCenter=true&width=640&lines=%24+kubectl+get+nodes+--all;%24+mysql+%3E+SHOW+REPLICA+STATUS%5CG;%24+shipping+React+%2B+TypeScript+to+prod;%24+building+systems+from+code+to+cluster" alt="typing intro"/></a>
</p>

<p align="center">
  <a href="https://linkedin.com/in/ayushshrestha85"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:ayushshrestha8585@gmail.com"><img src="https://img.shields.io/badge/Email-00F5D4?style=flat-square&logo=gmail&logoColor=0f2027" alt="Email"/></a>
  <img src="https://img.shields.io/badge/Kathmandu-Nepal%20🇳🇵-203a43?style=flat-square" alt="Location"/>
  <img src="https://img.shields.io/badge/Experience-4%2B%20years-203a43?style=flat-square" alt="Experience"/>
</p>

---

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

## `~ $ ls ./projects`

| Project | What it is | Tech |
| --- | --- | --- |
| **Fatafat** ([API](https://github.com/ayush85/fatafat-backend)) | E-commerce platform: Next.js storefront (private repo) on a Laravel REST API with Sanctum auth, products, cart, orders, reviews and Scribe docs | Next.js, Laravel, MySQL |
| [**Egg Farm Management**](https://egg-farm.aydexis.com) | Management platform for poultry and egg farm operations (live demo; source is private) | TypeScript |
| **Optix** | Small-tools and equipment tracking for construction: custody, jobsite assignment and an append-only ledger (private repo) | Next.js, Hono, tRPC, Drizzle, Postgres |
| [**Menuor**](https://github.com/ayush85/MoodMenu) | Multi-restaurant menu platform with per-restaurant custom domains, automated nginx and Let's Encrypt provisioning | Next.js, Prisma, Docker |
| [**aydexCloud**](https://github.com/ayush85/aydexCloud) | Privacy-focused web analytics: Go event tracker with a Next.js dashboard | Go, Next.js, Prisma |
| **Futsal Booking** | Court booking with customer, owner and admin roles and an approve/reject flow (private repo) | React, Express, Prisma |
| [**FinTrack**](https://github.com/ayush85/FinTrack) | React Native app that parses bank and wallet SMS into categorized spending summaries | React Native |

## `~ $ ./stats.sh`

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=ayush85&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&show_icons=true" alt="GitHub stats"/>
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ayush85&theme=tokyonight&hide_border=true&layout=compact" alt="Top languages"/>
</p>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:2c5364,100:0f2027&section=footer" alt=""/>
