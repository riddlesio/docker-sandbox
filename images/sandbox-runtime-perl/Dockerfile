FROM alpine:3.8

# https://pkgs.alpinelinux.org/packages?name=perl&branch=&repo=&arch=&maintainer=
ENV PERL_VERSION 5.26.2-r1
RUN apk update && \
    apk add --no-cache perl=${PERL_VERSION} && \
    rm -rf /var/cache/apk/*
