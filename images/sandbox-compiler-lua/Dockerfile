FROM alpine:3.6

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_lua.sh /riddles/compile_lua.sh

CMD "/riddles/compile_lua.sh"
