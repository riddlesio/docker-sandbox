FROM gcr.io/riddles-microservices/base:latest

# initialize package cache to be able to install packages
RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common wget make curl bzip2 libc6-dev pkg-config unzip \
    && rm -rf /var/lib/apt/lists/*

# Locale should be the same for matchrunner and sandbox
# Otherwise we'll get unicode errors when executing sandboxed commands
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install C/C++
RUN \
    add-apt-repository -y ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get install -y gcc-5 g++-5 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave /usr/bin/g++ g++ /usr/bin/g++-5

# Install Python
RUN apt-get -y install python3-pip

# Install Java
ENV JAVA_JDK jdk1.8.0
ENV JAVA_LINK 8u131-b11
ENV JAVA_VERSION 8u131
RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JAVA_LINK/d54c1d3a095b4ff2b6607d096fa80163/jdk-$JAVA_VERSION-linux-x64.tar.gz" && \
    tar -xvf jdk-$JAVA_VERSION-linux-x64.tar.gz && \
    mkdir /usr/lib/jvm && \
    mv $JAVA_JDK* /usr/lib/jvm/$JAVA_JDK && \
    update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/$JAVA_JDK/bin/java" 1 && \
    update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/$JAVA_JDK/bin/javac" 1 && \
    update-alternatives --install "/usr/bin/jar" "jar" "/usr/lib/jvm/$JAVA_JDK/bin/jar" 1 && \
    update-alternatives --set java /usr/lib/jvm/$JAVA_JDK/bin/java && \
    update-alternatives --set javac /usr/lib/jvm/$JAVA_JDK/bin/javac && \
    update-alternatives --set jar /usr/lib/jvm/$JAVA_JDK/bin/jar && \
    rm jdk-$JAVA_VERSION-linux-x64.tar.gz && \
    rm /usr/lib/jvm/$JAVA_JDK/src.zip && \
    rm /usr/lib/jvm/$JAVA_JDK/javafx-src.zip

# Install C#
RUN cd /tmp && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list && \
    apt-get update && \
    apt-get -y install mono-mcs

## Install Javascript
RUN cd /tmp && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install nodejs -y && \
    npm install -g npm@latest

## Install PHP
RUN cd /tmp && \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated php5.6

## Install D
ENV D_MAJOR 2.x
ENV D_VERSION 2.071.0
RUN cd /tmp && \
    apt-get install -y --no-install-recommends xdg-utils libcurl3 && \
    wget "http://downloads.dlang.org/releases/$D_MAJOR/$D_VERSION/dmd_$D_VERSION-0_amd64.deb" -O dmd_$D_VERSION-0_amd64.deb && \
    dpkg -i dmd_$D_VERSION-0_amd64.deb && \
    apt-get install -f -y && \
    rm dmd_$D_VERSION-0_amd64.deb

## Install Haskell
RUN \
    apt-get install -y haskell-platform

## Install Ruby
ENV RB_MAJOR 2.3
ENV RB_VERSION 2.3.1
RUN cd /tmp && \
    wget "https://cache.ruby-lang.org/pub/ruby/$RB_MAJOR/ruby-$RB_VERSION.tar.gz" -O ruby-$RB_VERSION.tar.gz && \
    tar -xvzf ruby-*.tar.gz && \
    cd ruby-$RB_VERSION/ && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf ruby-$RB_VERSION.tar.gz ruby-$RB_VERSION/

## Install Scala
ENV SCALA_VERSION 2.11.8
ENV SCALA_HOME /usr/lib
RUN cd /tmp && \
    wget "http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz" -O scala-$SCALA_VERSION.tgz && \
    tar -xvzf scala-$SCALA_VERSION.tgz && \
    mv scala-$SCALA_VERSION/ $SCALA_HOME && \
    rm scala-$SCALA_VERSION.tgz
ENV PATH $SCALA_HOME/scala-$SCALA_VERSION/bin:$PATH

## Install Lua
ENV LUA_VERSION 2.0.4
RUN cd /tmp && \
    wget "http://luajit.org/download/LuaJIT-$LUA_VERSION.tar.gz" -O LuaJIT-$LUA_VERSION.tar.gz && \
    tar -xvf LuaJIT-$LUA_VERSION.tar.gz && \
    cd LuaJIT-$LUA_VERSION && \
    make && \
    make install && \
    cd .. && \
    rm -rf LuaJIT-$LUA_VERSION.tar.gz LuaJIT-$LUA_VERSION

## Install Perl
ENV PERL_VERSION 5.24.0
RUN cd /tmp && \
    curl -SL "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/perl-$PERL_VERSION.tar.bz2" -o perl-$PERL_VERSION.tar.bz2 && \
    tar -xjf perl-$PERL_VERSION.tar.bz2 && \
    cd perl-$PERL_VERSION && \
    ./Configure -Duse64bitall -Duseshrplib -Dprefix=/usr -Dcc=gcc -des && \
    make && \
    make install && \
    rm /usr/bin/perl && \
    cp /usr/bin/perl$PERL_VERSION /usr/bin/perl

# Install Pascal
ENV PASCAL_VERSION 3.0.2
RUN cd /tmp && \
    wget "ftp://ftp.hu.freepascal.org/pub/fpc/dist/${PASCAL_VERSION}/x86_64-linux/fpc-${PASCAL_VERSION}.x86_64-linux.tar" -O fpc.tar && \
    tar xf "fpc.tar" && \
    cd "fpc-${PASCAL_VERSION}.x86_64-linux" && \
    rm demo* doc* && \
    ./install.sh && \
    find "/usr/lib/fpc/${PASCAL_VERSION}/units/x86_64-linux/" -type d -mindepth 1 -maxdepth 1 \
        -not -name 'fcl-base' \
        -not -name 'rtl' \
        -not -name 'rtl-console' \
        -not -name 'rtl-objpas' \
        -exec rm -r {} \;

# Install Go
# https://github.com/docker-library/golang/blob/64b88dc3e9d83e71eafc000fed1f0d5e289b3e65/1.8/Dockerfile
ENV GOLANG_VERSION 1.8.3
RUN set -eux; \
    \
# this "case" statement is generated via "update.sh"
    dpkgArch="$(dpkg --print-architecture)"; \
    case "${dpkgArch##*-}" in \
        ppc64el) goRelArch='linux-ppc64le'; goRelSha256='e5fb00adfc7291e657f1f3d31c09e74890b5328e6f991a3f395ca72a8c4dc0b3' ;; \
        i386) goRelArch='linux-386'; goRelSha256='ff4895eb68fb1daaec41c540602e8bb4c1e8bb2f0e7017367171913fc9995ed2' ;; \
        s390x) goRelArch='linux-s390x'; goRelSha256='e2ec3e7c293701b57ca1f32b37977ac9968f57b3df034f2cc2d531e80671e6c8' ;; \
        armhf) goRelArch='linux-armv6l'; goRelSha256='3c30a3e24736ca776fc6314e5092fb8584bd3a4a2c2fa7307ae779ba2735e668' ;; \
        amd64) goRelArch='linux-amd64'; goRelSha256='1862f4c3d3907e59b04a757cfda0ea7aa9ef39274af99a784f5be843c80c6772' ;; \
        *) goRelArch='src'; goRelSha256='5f5dea2447e7dcfdc50fa6b94c512e58bfba5673c039259fd843f68829d99fa6'; \
            echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a corresponding Go binary release; will be building from source"; echo >&2 ;; \
    esac; \
    \
    url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \
    wget -O go.tgz "$url"; \
    echo "${goRelSha256} *go.tgz" | sha256sum -c -; \
    tar -C /usr/local -xzf go.tgz; \
    rm go.tgz; \
    \
    if [ "$goRelArch" = 'src' ]; then \
        echo >&2; \
        echo >&2 'error: UNIMPLEMENTED'; \
        echo >&2 'TODO install golang-any from jessie-backports for GOROOT_BOOTSTRAP (and uninstall after build)'; \
        echo >&2; \
        exit 1; \
    fi; \
    \
    export PATH="/usr/local/go/bin:$PATH"; \
    go version
ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

# Install OCaml (version is default ubuntu version)
# TODO: use opam to build the latest version (takes a long time though)
ENV OCAML_VERSION=4.02.3
RUN apt-get install -y patch ocaml

# Install Kotlin
ENV KOTLIN_VERSION=1.1.2-2
ENV KOTLIN_HOME=/usr/local/kotlin
RUN cd /tmp && \
    wget -k "https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip"  && \
    unzip "kotlin-compiler-${KOTLIN_VERSION}.zip" && \
    mkdir -p "${KOTLIN_HOME}" && \
    mv "/tmp/kotlinc/bin" "/tmp/kotlinc/lib" "${KOTLIN_HOME}" && \
    rm ${KOTLIN_HOME}/bin/*.bat && \
    chmod +x ${KOTLIN_HOME}/bin/* && \
    ln -s "${KOTLIN_HOME}/bin/"* "/usr/bin/"

## Install Elixir (doesn't seem to work anymore)
#ENV ELIXIR_VERSION 1.2.6
#RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections  # See : https://github.com/phusion/baseimage-docker/issues/58
#RUN echo "deb http://packages.erlang-solutions.com/ubuntu trusty contrib" >> /etc/apt/sources.list && \
#    apt-key adv --fetch-keys http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc && \
#    apt-get -qq update && \
#    apt-get install -y esl-erlang
#RUN wget "https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb" && \
#    dpkg -i erlang-solutions_1.0_all.deb && \
#    rm erlang-solutions_1.0_all.deb && \
#    apt-get update && \
#    apt-get install -y elixir=$ELIXIR_VERSION*
#RUN mix local.hex --force && \
#    mix local.rebar --force
#
## Install Rust (this is working, but we are not supporting rust at the moment)
#ENV RUST_VERSION 1.9.0
#RUN \
#    curl -sO "https://static.rust-lang.org/dist/rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz" && \
#    tar -xzf rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz && \
#    ./rust-$RUST_VERSION-x86_64-unknown-linux-gnu/install.sh --without=rust-docs && \
#    rm -rf \
#        rust-$RUST_VERSION-x86_64-unknown-linux-gnu \
#        rust-$RUST_VERSION-x86_64-unknown-linux-gnu.tar.gz

# Cleanup
RUN rm -rf /tmp/*
RUN apt-get autoremove -y
#RUN apt-get remove --purge -y wget make curl bzip2 unzip
RUN apt-get clean