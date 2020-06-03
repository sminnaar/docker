FROM debian

ENV TS3DIR=/opt/TS3 TS3SERVER_LICENCE=accept

RUN apt update && apt upgrade -y && apt install bzip2 wget apt-utils ca-certificates -y && rm -rf /var/lib/apt/lists/* && wget https://files.teamspeak-services.com/releases/server/3.10.2/teamspeak3-server_linux_amd64-3.10.2.tar.bz2 -O /tmp/fuckinghell.tar.bz2 && tar jvxf /tmp/fuckinghell.tar.bz2 -C /opt && mv /opt/teamspeak3-server_* ${TS3DIR} && rm tmp/fuckinghell.tar.bz2 && groupadd -g 503 teamspeakadmin && useradd -u 503 -g 503 -d ${TS3DIR} teamspeakadmin && mkdir /data && chown -R teamspeakadmin:teamspeakadmin ${TS3DIR} /data

USER teamspeakadmin

WORKDIR ${TS3DIR}

ENTRYPOINT [ "sh", "ts3server_minimal_runscript.sh" ]

# Teamspeak files:
# https://files.teamspeak-services.com/releases/server/3.10.2/teamspeak3-server_linux_amd64-3.10.2.tar.bz2

# To start the server:
# docker run -dit --init --rm --name ts3server -p 9987:9987/udp -p 10011:10011 -p 30033:30033 ex01
