FROM debian:stretch-slim

# TODO: Create alpine image. Image now probably 300-400Mb too large

ENV LANG C.UTF-8

ENV D_MAJOR 2.x
ENV D_VERSION 2.075.0
RUN cd /tmp && \
    apt-get update && \
    apt-get install -y --no-install-recommends wget xdg-utils libcurl3 libc6-dev gcc && \
    wget "http://downloads.dlang.org/releases/$D_MAJOR/$D_VERSION/dmd_$D_VERSION-0_amd64.deb" -O dmd_$D_VERSION-0_amd64.deb && \
    dpkg -i dmd_$D_VERSION-0_amd64.deb && \
    apt-get install -f -y && \
    apt-get remove --purge -y wget && \
    rm dmd_$D_VERSION-0_amd64.deb

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_d.sh /riddles/compile_d.sh

CMD "/riddles/compile_d.sh"
