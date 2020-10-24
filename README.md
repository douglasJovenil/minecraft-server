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

## Mods
- Aether
- Skyblock
- Stoneblock
- Moonlight