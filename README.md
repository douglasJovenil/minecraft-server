# Minecraft Server Sky Block Docker

## Installing
```
git clone https://github.com/douglasJovenil/minecraft-server-docker
cd minecraft-server-docker/src
docker build -t ubuntu -f Dockerfile .
docker run -it -d --rm --name minecraft ubuntu
docker start minecraft
docker exec -it minecraft /bin/bash
```

## Running container
```
sudo docker-compose build
sudo docker-compode up -d
```

## SSH On GCloud

Open the file **/etc/ssh/sshd_config**, and change the following line :
```
PasswordAuthentication no
```
to:
```
PasswordAuthentication yes
```
then:
```
sudo service ssh restart
sudo adduser USERNAME
sudo usermod -aG sudo USERNAME
```