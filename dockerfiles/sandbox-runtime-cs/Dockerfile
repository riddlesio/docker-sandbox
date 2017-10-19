FROM alpine:3.6

# https://pkgs.alpinelinux.org/packages?name=mono&branch=&repo=&arch=&maintainer=
ENV MONO_VERSION 5.0.1.1-r0
RUN apk add mono=$MONO_VERSION --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \
    rm -rf /var/cache/apk/*
