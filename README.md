# 🏠 HomeLab

Welcome to the **HomeLab** branch of [⚓ Dockyard](https://github.com/JitendraSachwani/dockyard) — your personal self-hosted media server, automation hub, and home dashboard stack, powered by Docker.

This setup is designed for tech-savvy enthusiasts running on **Raspberry Pi**, **Intel NUC**, or any **home server**, and includes everything you need to manage, download, and stream content—all automatically.

##

## 📦 What's Inside?

This stack includes a full suite of tools for

### 📥 Download Automation

| Service        | Purpose                       | Port |
| -------------- | ----------------------------- | ---- |
| `qbittorrent`  | BitTorrent client             | 7001 |
| `nzbget`       | Usenet downloader             | 7002 |
| `transmission` | Alternative BitTorrent client | 7003 |

##

### 📁 Media Management

| Service    | Role         | Port |
| ---------- | ------------ | ---- |
| `prowlarr` | Indexer mgmt | 8002 |
| `radarr`   | Movies       | 8101 |
| `sonarr`   | TV Shows     | 8102 |
| `lidarr`   | Music        | 8103 |
| `readarr`  | Books        | 8104 |
| `bazarr`   | Subtitles    | 8201 |

##

### 📺 Streaming and Requests

| Service      | Function               | Port |
| ------------ | ---------------------- | ---- |
| `jellyfin`   | Media server           | 8000 |
| `jellyseerr` | Media request frontend | 8202 |

##

### 🍴 Extras

| Service    | Purpose                      | Port |
| ---------- | ---------------------------- | ---- |
| `mealie`   | Recipe manager               | 7101 |
| `postgres` | Database for Mealie          | 7005 |
| `homarr`   | Beautiful homepage/dashboard | 8080 |

##

### 🔐 Access Layer

| Service | Role                              |
| ------- | --------------------------------- |
| `newt`  | Pangolin client for reverse proxy |

> `newt` allows secure remote exposure of selected services via a [**Pangolin VPS proxy**](https://github.com/JitendraSachwani/dockyard/tree/proxy).

##

## ⚙️ Getting Started

Clone only this branch:

```bash
git clone --single-branch --branch homelab https://github.com/JitendraSachwani/mediaserver.git homelab
cd homelab
```

##

## 📌 Prerequisites

- Docker + Docker Compose

- `.env` file with secrets

- Media & downloads folder structure:

  - `/media/mediaserver`

  - `/media/mediaserver/MediaShare/Downloads`

##

## 🧪 Example .env

```bash
COMPOSE_PROFILES=prod
TZ=Etc/UTC

NEWT_ENDPOINT=https://your.vps.url
NEWT_ID=your_newt_id
NEWT_SECRET=your_newt_secret

DUPLICATI_ENC_KEY=your_encryption_key
HOMARR_ENC_KEY=your_homarr_secret

DOCKER_REGISTRY_USERNAME=your_registry_user
DOCKER_REGISTRY_PASSWORD=your_registry_pass

```

##

## 🚀 Run the Stack

Run all the services using:

```bash
# Set a Static IP (192.168.1.53) via GUI or use the following commands
nmcli connection modify "Wired connection 1" ipv4.method manual ipv4.addresses 192.168.1.53/24 ipv4.gateway 192.168.1.1 ipv4.dns "8.8.8.8 1.1.1.1"
nmcli connection down "Wired connection 1" && nmcli connection up "Wired connection 1"

docker compose up -d
```

Stop services:

```bash
docker compose down
```

> Any service can be tagged as a development service by adding `profiles: ["dev"]` to their attributes and then running them with `docker compose --profile dev up`

##

## 🤝 Contribute & Customize

This is a personal project, but you're welcome to fork it and adapt it to your needs. If you have ideas or improvements, feel free to open a pull request.

> **Happy Self-Hosting!** 🐳  
> _– Jitendra Sachwani_
