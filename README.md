# ⚓ Dockyard - Docker Setups Repository 🐳

Welcome to my ⚓ **Dockyard** 🐳

This is a centralized harbor for managing multiple Docker-based environments across my infrastructure.

This repository **uses branches** to organize different setups, while the `master` branch serves as a placeholder and reference point with documentation only.

##

## 📂 Branch Structure

### 🔹 [`homelab`](https://github.com/JitendraSachwani/dockyard/tree/homelab)

This branch contains the **HomeLab** setup — a self-hosted media server stack using Docker Compose. It includes:

- Portainer for container management
- Transmission / qBittorrent for downloads
- Radarr / Sonarr / Lidarr for automated content management
- Tautulli for media stats and analytics
- Watchtower for auto-updates
- Plex / Jellyfin for media streaming

Perfect for creating your own private media server running on a Raspberry Pi, NUC, or other home hardware.

## 

### 🔹 [`proxy`](https://github.com/JitendraSachwani/dockyard/tree/proxy)

This branch includes the configuration for a **remote VPS** that acts as a **Pangolin Reverse Proxy** to securely expose services from the HomeLab to the public internet.

- Pangolin for reverse proxying and TLS termination
- Fail2ban & UFW for basic security
- Dockerized setup for easy deployment on a low-cost VPS

This setup ensures secure and flexible remote access to HomeLab services.

## 

### 🔹 [`workstation`](https://github.com/JitendraSachwani/dockyard/tree/workstation)

This branch contains the setup for my primary **Windows Workstation** — primarily used for gaming and personal projects. It includes:

- Custom Rainmeter configuration
- Curated wallpaper collection
- Organized workspace base folder structure
- Handy macros and automation scripts

##


## 🛠️ Getting Started

To use any of these setups clone the specific dockyard branch:

```bash
git clone --single-branch --branch <dockyard_branch_name> https://github.com/JitendraSachwani/dockyard.git <local_folder_name>
```

Replace <dockyard_branch_name> with one of above mentioned branches and optionally specify a <local_folder_name> if you want to rename the directory locally.

## 

## 🧭 Why Branch-Based?

Using branches allows:

- Modular and independent setups

- Clean separation of environments

- Easier testing, collaboration, and version control

## 

## 📬 Feedback & Contributions

This is a personal project, but feel free to fork it, open issues, or suggest improvements. If you're running something similar, I’d love to hear how you’ve set yours up too!
