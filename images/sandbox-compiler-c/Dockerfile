FROM alpine:3.6

# https://pkgs.alpinelinux.org/packages?name=gcc&branch=&repo=&arch=&maintainer=
ENV GCC_VERSION 6.3.0-r4

RUN apk update && \
    apk add --no-cache gcc=$GCC_VERSION musl-dev && \
    rm -rf /var/cache/apk/*

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_c.sh /riddles/compile_c.sh

CMD "/riddles/compile_c.sh"
