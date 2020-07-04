# Use the latest alpine docker image
FROM alpine:latest

# In the alpine STDIN run these commands
RUN apk add --update vim && rm -rf /var/cache/apk/*

# Set current working directory
WORKDIR /home

# When started, run this command, as an example:
# CMD ["echo", "Hello"] will print "Hello" in STDOUT
CMD ["vim"]

# To build the image and tag(-t) it with the exercise nr:

# ``` sh
#		docker build -t alpine:ex00 .
# ```

# The last arg is the Dockerfile location(In this case "." or "current").

# To run the container:

# ``` sh
#		docker run -it --name ex00 -v /home/ex00/:/home alpine:ex00
# ```

# To run container in future:

# ``` sh
#		docker start -i ex00
# ```

# Any file saved with vim can be found at "/home/ex00/" on the docker-machine

# Run:

# ``` sh
#		docker-machine ssh Char
# ```
