FROM alpine:latest

RUN apk add --update vim htop && rm -rf /var/cache/apk/*

# CMD [ "htop" ]
CMD [ "vim" ]
# To build the image and tag(-t) it with the exercise nr:
# The last arg is the Dockerfile location(In this case "." or "current").

# docker build -t alpine:ex00 .

# To run the container:

# docker run -it --name ex00 alpine:ex00
