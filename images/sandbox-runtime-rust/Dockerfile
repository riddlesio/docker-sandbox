FROM alpine:3.8

RUN apk update && \
    apk add --no-cache llvm-libunwind libc-dev && \
    rm -rf /var/cache/apk/*
