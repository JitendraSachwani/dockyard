# 🌐 Proxy

Welcome to the **`proxy`** branch of the ⚓ Dockyard — a secure, containerized reverse proxy environment to expose your self-hosted services to the internet via a remote VPS.

This branch configures a hardened **reverse proxy gateway** using [Pangolin](https://github.com/fosrl/pangolin), designed to sit between your public-facing VPS and private HomeLab setup.

## 

## 📦 What's Inside?

This Docker Compose stack includes:

| Service     | Purpose                                 |
|-------------|-----------------------------------------|
| **Pangolin**| Authentication + control tunnel backend |
| **Gerbil**  | VPN-like tunnel endpoint with NAT       |
| **Traefik** | TLS termination + reverse proxy         |

> ✅ Ideal for exposing your internal homelab services to the internet through your VPS' public IP or domain name — without exposing your HomeLab directly.

##

## 🧱 Setup Overview

```plaintext
🌍   The Public Internet
              │
              ▼
🔐 [Traefik + Gerbil + Pangolin] (VPS)
              │
              ▼
🌐 Internal HomeLab Services (via secure newt tunnel)
```

##

## ⚙️ Getting Started

Clone only this branch:

```bash
git clone --single-branch --branch proxy https://github.com/JitendraSachwani/dockyard.git proxy
cd proxy
```

##

## 📌 Prerequisites

- Docker + Docker Compose

- `.env` file with secrets

##

## 🧪 Example .env

```bash
COMPOSE_PROFILES=prod
TZ=Etc/UTC

SERVER_SECRET=your-secure-server-secret # Can be generated using `openssl rand -base64 48`
USERS_SERVERADMIN_EMAIL=admin@example.com
USERS_SERVERADMIN_PASSWORD=super-secure-password
```

##

## 🚀 Run the Stack

Run all the services using:

```bash
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