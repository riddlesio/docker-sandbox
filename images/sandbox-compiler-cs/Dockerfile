FROM alpine:3.6

# https://pkgs.alpinelinux.org/packages?name=mono&branch=&repo=&arch=&maintainer=
ENV MONO_VERSION 5.2.0.224-r0
RUN apk add mono=$MONO_VERSION --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_cs.sh /riddles/compile_cs.sh

CMD ["./compile_cs.sh"]
