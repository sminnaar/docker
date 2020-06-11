FROM alpine

RUN apk update && apk add vim

# CMD vim the_file.c
ENTRYPOINT [ "vim" ]

# To build the image and tag(-t) it with the exercise nr:
# The last arg is the Dockerfile location(In this case "." or "current").

# docker build -t alpine:ex00 .

# To run the container:

# docker run -it --name ex00 alpine:ex00
