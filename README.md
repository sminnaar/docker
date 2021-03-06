# docker
The 42 school docker project

## Setup
1. Install docker, docker-machine and virtualbox
2. Run:
```bash
docker -v && docker-machine -v && virtualbox --help
```
If all the version numbers are printed it shows that the instalation succeded


## 00_how_to_docker

These commands can all be run with the following bash commands replacing "01" with the exercise number:
```bash
while read command; do echo $command && $command; done < 01
```
OR
```bash
cat 01 | bash
```
### Explinations of the commands:
01. Create a virtual machine with docker-machine, (--driver) use the virtualbox driver and (--name) name it Char
    ```bash
    docker-machine create --driver virtualbox Char
    ```

02. Get the IP of Char
    ```bash
    docker-machine ip Char
    ```

03. Set DOCKER ENV varialbles to console environment.
    - Note: commands with $( ) as arguments tend to break with the "while do" and "cat 27 | bash" commands. Might want to run them manually.

    - Run this before and after running command 03:
    ```bash
    env | grep DOCKER
    ```
    ```bash
    eval $(docker-machine env Char)
    ```

04. Pull the hello-world docker image from docker hub
    ```bash
    docker pull hello-world
    ```

05. Launch the hello-world container
    ```
    docker run hello-world
    ```
06. Launch a container, set restart varible, (-p) bind port 80 to docker-machine port 5000, (-d) detach, (--name) name it overlord and use the nginx image.
    - Use { docker-machine-ip } : { 5000 }  in browser to test
    ```bash
    docker run --restart=always -p 5000:80 -d --name overlord nginx
    ```

07. Inspecting a contaner returns a .JSON with the IP as an attribute -f formats the output and only prints the IP of the container
    ```bash
    docker inspect -f '{{.NetworkSettings.IPAddress}}' overlord
    ```

08. Launch a container with the alpine:latest as base, (-it ) launch an interactive terminal to be able to execute commands in the contaner shell and (--rm) when exited stop container.
    - Note: This command does not work with the "while do" and "cat 27 | bash" commands as it needs to bind your terminal to the container terminal.
    ```bash
    docker run -it --rm alpine
    ```

09. Run container with debian running, (-it) open a shell terminal, (--rm) remove itself when exited.
    - Note: This command does not work with the "while do" and "cat 27 | bash" commands as it needs to bind your terminal to the container terminal.
    - These commands should be run in the docker machine's terminal, they will update the libraries and install gcc, vim and git.
    ```bash
    apt-get update && apt-get install -y gcc vim git
    ```
    ```bash
    docker run -it --rm debian
    ```

10. Create a docker volume named hatchery this is allocateble storage for your containers to use. In this case it will be used by the mysql docker container.
    ```bash
    docker volume create --name hatchery
    ```

11. List the docker volumes. If there are containers running, their disk space will be displayed as an unnamed volume.
    ```bash
    docker volume ls
    ```

12. Launch a mysql container, (-d) detach, set restart, (-p) bind port 3306 of docker-machine to port 3306 of container, (-v) attach volume, (-e) set environmental variables, (--name) name it and use the mysql:latest image.
    ```bash
    docker run -d --restart=on-failure -p 3306:3306 -v hatchery:/var/lib/mysql -e MYSQL_DATABASE=zerglings -e MYSQL_ROOT_PASSWORD=Kerrigan --name spawning-pool mysql
    ```
13. Execute the env command in the spawning-pool container shell.
    ```bash
    docker exec spawning-pool env
    ```

14. Run a docker container, (-d) detatch, (--name) name it, (-p) bind port 8080 of the docker-machine to port 80 of the container, (--link) import env from a container as :tag, (-e) set env variables and use the wordpress image.
    ```bash
    docker run -d --name lair -p 8080:80 --link spawning-pool:mysql -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASS=Kerrigan -e WORDPRESS_DB_HOST=mysql -e MYSQL_PORT_3306_TCP=3306  wordpress
    ```

15. Run a docker container, (-d) detatch, (-p) bind port 8081 of the docker-machine to port 80 of the container, (--link) import env variables from spawning-pool with prefix db, (--name) name it and use the phpmyadmin image.
    ```bash
    docker run -d -p 8081:80 --link spawning-pool:db --name roach-warden phpmyadmin/phpmyadmin
    ```

16. Display the logs of a docker container
    - Note: This command does not work with the "while do" and "cat 27 | bash" commands as it needs to bind your terminal to the container terminal.
    ```bash
    docker logs spawning-pool
    ```

17. List the docker containers
    ```bash
    docker container ls
    ```

18. Restart a docker container
    ```bash
    docker restart overlord
    ```

19. Run a docker container, (-d) run detached, (-p) bind it to a port, 3000 of docker-machine to 3000 of container, (--name) name it, (-v) link physical space on host, (-e) set environmental variables, (-w) set working dir, use the python:2-slim image, (bash) use bash to (-c) run commands inside the container. The commands will: update apt repository, upgrade it replying with (-y) yes to prompts, use pip to install flask and run flask with the host at 0.0.0.0 and bind it to port 3000 of the container.
    - Note: This command does not work with the "while do" and "cat 27 | bash" commands as it interpretes the quotes in a weird way.
    ```bash
    docker run -d -p 3000:3000 --name Abathur -v /home/:/root -e FLASK_APP=app.py -w /root python:2-slim bash -c "apt update && apt upgrade -y && python -m pip install --upgrade pip && pip install flask && flask run -h 0.0.0.0 -p 3000"
    ```

    - Note: app.py needs to be created with the following content and then copied into the container.
    ```bash
    from flask import Flask

    app = Flask(__name__)
    @app.route('/')
    def msg():
    return '<marquee><h1>Hello World</h1><h2>Hello World</h2><h3>Hello World</h3><h4>Hello World</h4><h5>Hello World</h5><h6>Hello World</h6><h7>Hello World</h7></marquee>'
    ```

    - Wait for the docker to finish installing the pacages then run the following command to copy the app.py file into the container. The file will be at root on the Char virtual-machine.
    ```bash
    docker cp app.py Abathur:/root
    ```
    - To display the logs of the container and (-f) bind the terminal to it run:
    ```bash
    docker logs -f Abathur
    ```

20. Initialise a docker swarm, (--advertise-addr) advertise its address as a string and bind it to the docker-machine port 2377. The ${ } will resolve to the Char docker-machine IP.
    - Note: commands with $( ) as arguments tend to break with the "while do" and "cat 27 | bash" commands. Might want to run them manually.
    ```bash
    docker swarm init --advertise-addr $(docker-machine ip Char):2377
    ```
    - Note: Only use port 2377 or leave it blank to use default(2377).
    - To test:
    ```bash
    docker node ls
    ```

21. Create a docker-machine (VM), (--driver) user a specific driver and name it Aiur.
    ```bash
    docker-machine create --driver virtualbox Aiur
    ```

22. ssh into a Docker-Machine VM.
    ```bash
    docker-machine ssh Aiur "docker swarm join --token SWMTKN-1-3vf7l9thkaljcl3imhogax7aybwd4n49zxo356kjxznc062mdk-6chq7q4x5hu0w1dsks13hniuy 192.168.99.106:2377"
    ```
    - Note: The output of exercise 20 should be run in the Aiur docker-machine to connect it to the swarm.
    - This can be done with the following command, replacing the quotes with the output of exercise 20:
    ```bash
    docker-machine ssh Aiur "docker swarm join --token SWMTKN-1-1mj6eb92fz2opie040il53ft2a5b5l3ze8dsnuwmy5mlsqcsm0-8vb1wedtb2fjtz1mjzejkm5kd 192.168.99.104:2377"
    ```

23. Create a docker network of (--driver) overlay type and name it overmind.
    ```bash
    docker network create --driver overlay overmind
    ```

24. Launch a docker service (a container connected in a swarm) with, (-e) set environmental variables, (--name) name it, (--network) connect it and use the rabbitmq image.
    ```bash
    docker service create -e RABBITMQ_DEFAULT_USER=commander -e RABBITMQ_DEFAULT_PASS=Kerrigan --name orbital-command --network overmind rabbitmq
    ```

25. List docker services.
    ```bash
    docker service ls
    ```

26. Create a docker service (a container runninng in a swarm) with, (-e) environmental variables, (--replicas) duplicate the service, (--network) connect to a swarm network, (--name) name it and use the 42school/engineering-bay image.
    - Note: Checking the logs of the service when created without any environmental variables reveals the need for them nl: OC_USERNAME and OC_PASSWD
    ```bash
    docker service create -e OC_USERNAME=commander -e OC_PASSWD=Kerrigan --replicas 2 --network overmind --name engineering-bay 42school/engineering-bay
    ```

27. ssh into the swarm leader and run a command:  
Displays the logs of a docker service. (-f) Follow, continue streaming the new output from the service's STDOUT and STDERR. The $() returns the id of the ".1" replica of the engineering bay service. Omit the (-f) flag to include all replicas of the service.
    - Note: commands with $( ) as arguments tend to break with the "while do" and "cat 27 | bash" commands. Might want to run them manually.
    ```bash
    docker-machine ssh Char "docker service logs -f $(docker service ps engineering-bay -f 'name=engineering-bay.1' -q)"
    ```

28. Create a docker service, (-e) set environmental variable, (--replicas) create replicas, (--network) connect to a network, (--name) name it and use the 24school/marine-squad image.
    ```bash
    docker service create -e OC_USERNAME=commander -e OC_PASSWD=Kerrigan --replicas 2 --network overmind --name marines 42school/marine-squad
    ```

29. Display docker service tasks.
    ```bash
    docker service ps marines
    ```

30. Scale (increase or decrease) a docker service.
    ```bash
    docker service scale marines=20
    ```

31. Stop and remove a docker service. The $( ) returns the id's of all docker sevices. (ls) List, (-q) quite, returns service id only.
    - Note: commands with $( ) as arguments tend to break with the "while do" and "cat 31 | bash" commands. Might want to run them manually.
    ```bash
    docker service rm $(docker service ls -q)
    ```

32. Remove docker container, (-f) force. The $() varible will return (ps) info about containers (-a) all and (-q) quite: only return container id's.
    - Note: commands with $( ) as arguments tend to break with the "while do" and "cat 32 | bash" commands. Might want to run them manually.
    ```bash
    docker rm -f $(docker ps -a -q)
    ```

33. Remove docker image (-f) force removal. The $() variable will return info of all docker images. (-q) Quite, only return id's.
    - Note: commands with $( ) as arguments tend to break with the "while do" and "cat 33 | bash" commands. Might want to run them manually.
    ```bash
    docker rmi -f $(docker images -q)
    ```

34. Stop and (rm) remove/delete a Docker machine, (-y) auto select yes for prompt.
    ```bash
    docker-machine rm -y Aiur
    ```

## 01_dockerfiles

>## 1. ex00
>
>- To build the image and tag(-t) it with the exercise nr:
>
>``` sh
>docker build -t alpine:ex00 .
>```
>
>- The last arg is the Dockerfile location(In this case "." or "current").
>
>- To run the container and (-v) bind its /home directory to /home/ex00/ of the docker-machine run:
>``` sh
>docker run -it --name ex00 -v /home/ex00/:/home alpine:ex00
>```
>
>- To run container in future:
>
>``` sh
>docker start -i ex00
>```
>
>- Any file saved with vim can be found at "/home/ex00/" on the docker-machine
>
>- Run this command and navigate to the /home/ex00/ directory:
>
>``` sh
>docker-machine ssh Char
>```
>

>## 2. ex01
>
>The Team Speak server .tar can be found here: [TeamSpeak .tar](https://files.teamspeak-services.com/releases/server/3.12.1/teamspeak3-server_linux_amd64-3.12.1.tar.bz2)
>
>- To build the image:
>```bash
>docker build -t debian:ex01 .
>```
>
>- To run the container:
>```bash
>docker run -it --init --rm --name ts_server -p 9987:9987/udp -p 10011:10011 -p 30033:30033 debian:ex01
>```
>
>- To get the password and privilege key run:
>```bash
>docker logs ts_server
>```
>- Start the teamspeak client and connect using $(docker-machine ip Char):9987 as Address.
>

>## 3. ex02
>
>To build first image:
>``` sh
>docker build -t ft-rails:on-build .
>```
>Dokerfile (from exersise):  
>```bash
>FROM	ft-rails:on-build
>
>EXPOSE 3000  
>CMD ["rails", "s", "-b", "0.0.0.0", "-p", "3000"]
>```
>
>To generate the second Dockerfile:
>``` sh
>{ echo "FROM ft-rails:on-build"; echo "EXPOSE 3000"; echo "CMD [ \"rails\", \"s\", \"-b\", \"0.0.0.0\", \"-p\",\"3000\" ]";} > app/Dockerfile
>```
>
>To build second Dockerfile:
>``` sh
>docker build -t rails:ex02 ./app
>```
>To run second Dockerfile:
>``` sh
>docker run --rm -p 3000:3000 rails:ex02
>```
>