FROM alpine:3.6

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_lua.sh /riddles/compile_lua.sh

CMD ["./compile_lua.sh"]
