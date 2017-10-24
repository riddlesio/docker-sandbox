FROM alpine:3.6

# https://hub.docker.com/r/frolvlad/alpine-fpc/~/dockerfile/

ENV FPC_VERSION 3.0.2
RUN apk add --no-cache binutils libgcc && \
    cd /tmp && \
    wget "ftp://ftp.hu.freepascal.org/pub/fpc/dist/${FPC_VERSION}/x86_64-linux/fpc-${FPC_VERSION}.x86_64-linux.tar" -O fpc.tar && \
    tar xf "fpc.tar" && \
    cd "fpc-${FPC_VERSION}.x86_64-linux" && \
    rm demo* doc* && \
    \
    # Workaround musl vs glibc entrypoint for `fpcmkcfg`
    mkdir /lib64 && \
    ln -s /lib/ld-musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \
    \
    echo -e '/usr\nN\nN\nN\n' | sh ./install.sh && \
    rm -rf /lib64 /tmp/* /var/cache/apk/* && \
    find "/usr/lib/fpc/${FPC_VERSION}/units/x86_64-linux/" -type d -mindepth 1 -maxdepth 1 \
        -not -name 'fcl-base' \
        -not -name 'rtl' \
        -not -name 'rtl-console' \
        -not -name 'rtl-objpas' \
        -exec rm -r {} \;

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_pascal.sh /riddles/compile_pascal.sh

CMD "/riddles/compile_pascal.sh"
