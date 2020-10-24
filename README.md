# Minecraft Server Docker


## Installing
```
git clone https://github.com/douglasJovenil/minecraft-server-docker
cd minecraft-server-docker/src
docker build -t ubuntu -f Dockerfile .
docker run -it -d --rm --name minecraft ubuntu
docker start minecraft
docker exec -it minecraft /bin/bash
```

## Setup machine

- Download the lastest version of Java from http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
- Transfer the file to cloud machine
- copy the file to **/opt**
```
sudo mv JAVAFILE.tax.gz /opt
cd /opt
sudo tar -zxvf JAVAFILE.tar.gz
sudo rm JAVAFILE.tar.gz
sudo update-alternatives --install /usr/bin/java java /opt/JAVAFOLDER/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /opt/JAVAFOLDER/bin/javac 1
```

In the steps bellow be shore to choose the version that you installed:
```
sudo update-alternatives --config java
sudo update-alternatives --config javac
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

## Mods
- Aether
- Skyblock
- Stoneblock
- Moonlight