FROM alpine:3.8

ENV RUST_VERSION 1.26.2-r0
ENV CARGO_VERSION 1.26.2-r0
RUN apk update && \
    apk add --no-cache gcc rust=${RUST_VERSION} cargo=${CARGO_VERSION} && \
    rm -rf /var/cache/apk/*

# this part is for adding some (offline) packages
ENV USER root
RUN cd tmp/ && \
    apk update && apk add --virtual build-deps perl make openssl openssl-dev cmake && \
    cargo install cargo-local-registry && \
    cargo new depdummy && \
    cd depdummy && \
    printf 'libc = "0.2.26"\nrand = "0.3.15"' >> Cargo.toml && \
    cargo build && \
    cargo local-registry --sync Cargo.lock /root/.cargo/bin && \
    printf "[source.crates-io]\nregistry = 'https://github.com/rust-lang/crates.io-index'\nreplace-with = 'local-registry'\n\n[source.local-registry]\nlocal-registry = '/root/.cargo/bin'" >> /root/.cargo/config && \
    apk del build-deps && \
    rm -rf /tmp/depdummy /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_rust.sh /riddles/compile_rust.sh

CMD ["./compile_rust.sh"]
