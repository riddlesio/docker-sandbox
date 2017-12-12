FROM alpine:3.6

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

ENV KOTLIN_VERSION 1.1.2-2
ENV KOTLIN_HOME /usr/lib/kotlin
RUN apk update && \
    apk add bash && \
    apk add --virtual build-deps wget ca-certificates && \
    cd /tmp && \
    wget "https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip" && \
    unzip "kotlin-compiler-${KOTLIN_VERSION}.zip" && \
    mkdir "${KOTLIN_HOME}" && \
    mv "/tmp/kotlinc/bin" "/tmp/kotlinc/lib" "${KOTLIN_HOME}" && \
    ln -s "${KOTLIN_HOME}/bin/"* "/usr/bin/" && \
    apk del build-deps && \
    rm -rf /tmp/* /var/cache/apk/*

RUN mkdir -p /tmp/riddles/compiler
RUN mkdir /riddles
WORKDIR /riddles

COPY compile_kotlin.sh /riddles/compile_kotlin.sh

CMD ["./compile_kotlin.sh"]
