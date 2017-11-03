FROM elixir:1.5.2-alpine

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_elixir.sh /riddles/compile_elixir.sh

CMD ["compile_elixir.sh"]
