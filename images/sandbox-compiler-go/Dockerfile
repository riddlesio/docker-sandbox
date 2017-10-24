FROM golang:1.9.1-alpine3.6

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_go.sh /riddles/compile_go.sh

CMD "/riddles/compile_go.sh"
