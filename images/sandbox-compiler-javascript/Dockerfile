FROM alpine:3.6

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_javascript.sh /riddles/compile_javascript.sh

CMD ["./compile_javascript.sh"]
