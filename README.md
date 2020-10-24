# Minecraft Server Sky Block Docker

## Installing
```
git clone https://github.com/douglasJovenil/minecraft-server-docker
```

## Running container
```
cd minecraft-server-docker/src
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
