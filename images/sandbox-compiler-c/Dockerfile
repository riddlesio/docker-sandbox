FROM alpine:3.8

# https://pkgs.alpinelinux.org/packages?name=gcc&branch=&repo=&arch=&maintainer=
ENV GCC_VERSION 6.4.0-r8

RUN apk update && \
    apk add --no-cache gcc=$GCC_VERSION musl-dev && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_c.sh /riddles/compile_c.sh

CMD ["./compile_c.sh"]
