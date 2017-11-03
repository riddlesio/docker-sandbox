FROM alpine:3.6

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_php.sh /riddles/compile_php.sh

CMD ["compile_php.sh"]
