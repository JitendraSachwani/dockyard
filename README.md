# My Media Server Setup

## Pre-Requisites

1. Setup docker (https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

```
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done


# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

```

Test docker installation with 
```
sudo docker run hello-world
```

Note: Add other users to the docker group for granting permissions to access docker socket
```
sudo usermod -a -G docker jenkins
```

## Start the Media Server

```
docker swarm init

# openssl rand -hex 32
echo "HOMARR_ENC_KEY" | sudo  docker secret create homarr_enc_key -

docker deploy --compose-file compose.yml mediaserver
```