FROM alpine:3.8

ENV GPP_VERSION 6.4.0-r8
RUN apk update && \
    apk add --no-cache g++=$GPP_VERSION musl-dev && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_cpp.sh /riddles/compile_cpp.sh

CMD ["./compile_cpp.sh"]
