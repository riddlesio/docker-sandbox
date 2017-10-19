FROM gcr.io/testriddles/alpine-java-runtime:1.0

# https://hub.docker.com/r/frolvlad/alpine-scala/~/dockerfile/

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
