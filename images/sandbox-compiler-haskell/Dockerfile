FROM debian:stretch-slim

# TODO: Create (small) alpine image

ENV LANG C.UTF-8

# Install Haskell (no easy way to install specific version)
RUN apt-get update && \
    apt-get install -y haskell-platform

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_haskell.sh /riddles/compile_haskell.sh

CMD "/riddles/compile_haskell.sh"
