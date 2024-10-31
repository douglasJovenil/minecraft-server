FROM alpine:3.19

ARG MINECRAFT_VERSION="1.20.6-50.1.0"
ARG MINECRAFT_INSTALLER_URL="https://maven.minecraftforge.net/net/minecraftforge/forge/${MINECRAFT_VERSION}/forge-${MINECRAFT_VERSION}-installer.jar"
ARG USER="minecraft"
ARG WORKDIR="/server"

WORKDIR ${WORKDIR}

COPY server.properties .

    # Instala o JDK
RUN apk add --no-cache openjdk21-jre-headless && \
    # Instala o servidor
    wget ${MINECRAFT_INSTALLER_URL} -O installer.jar && \
    java -jar installer.jar --installServer && \
    # Gera arquivo eula
    echo "eula=true" > eula.txt && \
    # Remove arquivos desnecessários
    rm installer.jar installer.jar.log && \
    # Adiciona o usuário e grupo
    addgroup -g 1000 ${USER} && \
    adduser -u 1000 -G ${USER} -s /bin/sh -D ${USER} && \
    chown -R ${USER}:${USER} ${WORKDIR}

USER ${USER}

ENTRYPOINT ["./run.sh"]