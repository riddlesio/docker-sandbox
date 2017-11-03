FROM alpine:3.6

# https://hub.docker.com/r/frolvlad/alpine-scala/~/dockerfile/

ENV JAVA_VERSION 8u131
ENV JAVA_ALPINE_VERSION 8.131.11-r2
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

ENV SCALA_VERSION=2.12.0
ENV SCALA_HOME=/usr/lib/scala

RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
	apk add --no-cache bash && \
	cd "/tmp" && \
	wget "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" && \
	tar xzf "scala-${SCALA_VERSION}.tgz" && \
	mkdir "${SCALA_HOME}" && \
	rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \
	mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" && \
	ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \
	apk del .build-dependencies && \
	rm -rf /tmp/* /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_scala.sh /riddles/compile_scala.sh

CMD ["compile_scala.sh"]
