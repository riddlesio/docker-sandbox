FROM alpine:3.6

# https://pkgs.alpinelinux.org/packages?name=perl&branch=&repo=&arch=&maintainer=
ENV PERL_VERSION 5.24.1-r2
RUN apk update && \
    apk add --no-cache perl=${PERL_VERSION} && \
    rm -rf /var/cache/apk/*
