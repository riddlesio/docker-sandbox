FROM debian:stretch-slim

# TODO: get this to work on alpine

ENV LANG C.UTF-8

RUN set -ex; \
	if ! command -v gpg > /dev/null; then \
		apt-get update; \
		apt-get install -y --no-install-recommends \
			gnupg2 \
			dirmngr \
		; \
		rm -rf /var/lib/apt/lists/*; \
	fi



ENV NODE_MAJOR 8
# npm 4.1.2 needed for Reason installation. Latest 5.3.0 doesn't work for some reason
ENV NPM_VERSION 4.1.2
RUN cd /tmp && \
    apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_$NODE_MAJOR.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@$NPM_VERSION && \
    apt-get remove -y curl

ENV OCAML_VERSION 4.02.3
RUN cd /tmp && \
    apt-get install -y wget patch ocaml unzip m4 make aspcud && \
    wget 'https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh' -O - | sh -s /usr/local/bin && \
    opam init -a && \
    opam switch $OCAML_VERSION && \
    eval $(opam config env) && \
    opam update && \
    apt-get remove -y wget

ENV REASON_VERSION 1.13.6
RUN apt-get update && \
    npm install -g https://github.com/reasonml/reason-cli/archive/beta-v-$REASON_VERSION-bin-linux.tar.gz && \
    npm cache clean && \
    \
    # uninstall node & npm
    apt-get remove -y nodejs && \
    rm -rf /usr/lib/node_modules/npm /usr/lib/nodejs /usr/include/node /usr/include/nodejs /usr/bin/node /usr/bin/nodejs /tmp/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_reason.sh /riddles/compile_reason.sh

CMD ["compile_reason.sh"]
