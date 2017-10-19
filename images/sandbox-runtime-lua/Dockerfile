FROM gcr.io/testriddles/alpine-base:1.0

ENV LUA_VERSION 5.3
RUN apk update && \
    apk add lua${LUA_VERSION} lua${LUA_VERSION}-dev && \
    cd /usr/bin && \
    ln -s lua${LUA_VERSION} lua && \
    rm -rf /var/cache/apk/*
