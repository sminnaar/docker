FROM alpine

RUN apk update && apk add vim

ENTRYPOINT [ "vim" ]

# To build the image and tag(-t) it with the exercise nr:
# ``` sh
# docker build -t alpine:ex00 .
#```
# The last arg is the Dockerfile location(In this case "." or "current").
