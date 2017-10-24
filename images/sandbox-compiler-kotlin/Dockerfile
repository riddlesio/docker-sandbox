FROM alpine:3.6

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

RUN mkdir /riddles
WORKDIR /riddles

COPY compile_kotlin.sh /riddles/compile_kotlin.sh

CMD "/riddles/compile_kotlin.sh"
