FROM debian:stretch-slim

# TODO: Create (small) alpine image

ENV LANG C.UTF-8

# Install Haskell (no easy way to install specific version)
RUN apt-get update && \
    apt-get install -y haskell-platform

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_haskell.sh /riddles/compile_haskell.sh

CMD ["./compile_haskell.sh"]
