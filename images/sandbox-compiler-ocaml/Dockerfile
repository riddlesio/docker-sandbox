FROM alpine:3.6

ENV OCAML_VERSION 4.04.1
RUN apk update && \
    apk add --virtual build-deps make && \
    apk add --no-cache opam ocamlbuild gcc musl-dev && \
    opam init -a && \
    opam switch $OCAML_VERSION && \
    eval $(opam config env) && \
    opam update && \
    apk del build-deps && \
    rm -rf /var/cache/apk/*

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_ocaml.sh /riddles/compile_ocaml.sh

CMD "/riddles/compile_ocaml.sh"
