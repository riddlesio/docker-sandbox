FROM alpine:3.6

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_python3.sh /riddles/compile_python3.sh

CMD ["./compile_python3.sh"]
