FROM alpine:3.8

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_ruby.sh /riddles/compile_ruby.sh

CMD ["./compile_ruby.sh"]
