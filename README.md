# 🧱 Dockyard: NAS Stack ⚓

Welcome to the **NAS branch** of [⚓ Dockyard](https://github.com/JitendraSachwani/dockyard) — the backbone of your NAS infrastructure, acting as a **centralized data and database host** for your HomeLab.

This stack is designed to provide **secure, isolated, and maintainable database services** across multiple hosts using **Docker Swarm** and **overlay networking** — without exposing any ports on the NAS itself.

##

## 📦 What's Inside?

This NAS setup includes a **multi-database stack**, each running as a service in Docker:

### 🗄️ Database Services

| Database       | Image         | Port            | Purpose                                   |
| -------------- | ------------- | --------------- | ----------------------------------------- |
| **MongoDB**    | `mongo:8`     | _internal only_ | NoSQL document store                      |
| **MySQL**      | `mysql:8.4`   | _internal only_ | Relational database for apps and services |
| **PostgreSQL** | `postgres:17` | _internal only_ | Advanced SQL database                     |
| **Redis**      | `redis:7.4`   | _internal only_ | Caching, session storage, and queues      |

Each service is part of a **shared overlay network (`db_net`)**, which allows other Docker hosts (e.g., backend servers) to access the databases securely _without exposing any host ports_.

##

### 🧭 Networking Architecture

```mermaid
graph LR
    A[External Host(s)] -->|db_net overlay| B[NAS Host]
    B --> Mongo[(MongoDB)]
    B --> MySQL[(MySQL)]
    B --> Postgres[(PostgreSQL)]
    B --> Redis[(Redis)]
```

Communication happens entirely within the **Docker Swarm overlay network** `db_net`.  
No direct database ports (27017, 3306, 5432, 6379) are published to the NAS host.

##

## ⚙️ Getting Started

### 📌 Prerequisites

- Docker + Docker Compose

- `.env` file with secrets

##

### 🔐 `.env` Configuration

The `.env` file is excluded from Git and contains your database credentials and defaults.

Example:

```bash
COMPOSE_PROFILES=prod
TZ=Asia/Kolkata

# MySQL
MYSQL_ROOT_PASSWORD=changeme
MYSQL_DATABASE=appdb
MYSQL_USER=appuser
MYSQL_PASSWORD=apppass

# PostgreSQL
POSTGRES_PASSWORD=changeme
POSTGRES_USER=appuser
POSTGRES_DB=appdb

# MongoDB
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=changeme

```

##

### 🚀 Deployment

#### 1️⃣ Clone only this branch:

```bash
git clone --single-branch --branch nas https://github.com/JitendraSachwani/dockyard.git homelab
cd nas
```

#### 2️⃣ Initialize Docker Swarm

```bash
docker swarm init --advertise-addr <NAS_LAN_IP>
```

#### 3️⃣ Create the Shared Overlay Network

```bash
docker network create --driver overlay --attachable db_net
```

#### 4️⃣ Get the Join Token (for external hosts)

```bash
docker swarm join-token worker
```

Copy the `docker swarm join ...` command and run it on your external host(s).

#### 5️⃣ Deploy the Stack

```bash
docker stack deploy -c compose.yml nas
```

Or, if you prefer standalone Compose:

```bash
docker compose up -d
```

##

### 🧠 Access from Other Hosts

Once your backend host has joined the Swarm (`docker swarm join ...`):

Launch your backend container and attach it to the same overlay network:

```bash
docker run -d --name app --network db_net myapp:latest
```

Then, inside that container, you can connect via:

MongoDB → `mongo_db:27017`

MySQL → `mysql_db:3306`

PostgreSQL → `postgres_db:5432`

Redis → `redis_db:6379`

✅ No host ports exposed

✅ Secure, internal-only traffic

##

## 🤝 Contribute & Customize

This is a personal project, but you're welcome to fork it and adapt it to your needs. If you have ideas or improvements, feel free to open a pull request.

> **Happy Self-Hosting!** 🐳  
> _– Jitendra Sachwani_
