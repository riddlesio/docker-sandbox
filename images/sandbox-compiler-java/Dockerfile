FROM alpine:3.8

ENV JAVA_VERSION 8u171
ENV JAVA_ALPINE_VERSION 8.171.11-r0
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home && \
	chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

RUN set -x && \
	apk add --no-cache openjdk8="$JAVA_ALPINE_VERSION" && \
	[ "$JAVA_HOME" = "$(docker-java-home)" ] && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_java.sh /riddles/compile_java.sh

CMD ["./compile_java.sh"]
