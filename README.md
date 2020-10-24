# Minecraft Server Sky Block Docker

## Installing
```
git clone https://github.com/douglasJovenil/minecraft-server-docker
cd minecraft-server/src
sudo docker-compose build
```

## Running container
```
sudo docker-compose up -d
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
