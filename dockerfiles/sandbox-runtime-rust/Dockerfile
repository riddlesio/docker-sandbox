FROM alpine:3.6

RUN apk update && \
    apk add --no-cache llvm-libunwind libc-dev && \
    rm -rf /var/cache/apk/*
