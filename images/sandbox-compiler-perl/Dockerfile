FROM alpine:3.8

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_perl.sh /riddles/compile_perl.sh

CMD ["./compile_perl.sh"]
