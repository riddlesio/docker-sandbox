FROM gcr.io/riddles-microservices/base:152e46c-cd3675d3cf07

# initialize package cache to be able to install packages
RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gnupg2 dirmngr software-properties-common wget make curl bzip2 libc6-dev pkg-config unzip cmake \
    \
#   rust stuff
    openssl libssl-dev \
    \
    && rm -rf /var/lib/apt/lists/*

# Locale should be the same for matchrunner and sandbox
# Otherwise we'll get unicode errors when executing sandboxed commands
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install C/C++
ENV GCC_VERSION 7.1
ENV GCC_MAJOR 7
RUN \
    add-apt-repository -y ppa:jonathonf/gcc-$GCC_VERSION && \
    apt-get update && \
    apt-get install -y gcc-$GCC_MAJOR g++-$GCC_MAJOR && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-$GCC_MAJOR 60 --slave /usr/bin/g++ g++ /usr/bin/g++-$GCC_MAJOR

# Install Python (https://github.com/docker-library/python/blob/88ba87d31a3033d4dbefecf44ce25aa1b69ab3e5/3.5/Dockerfile)
ENV PYTHON_VERSION 3.5.3
ENV PYTHON_PIP_VERSION 9.0.1
ENV GPG_KEY 97FC712E4C024BBEA48A61ED3A5CA953F73C700D
RUN set -ex \
    && buildDeps=' \
        dpkg-dev \
        tcl-dev \
        tk-dev \
    ' \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
    \
    && wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
    && wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \
    && gpg --batch --verify python.tar.xz.asc python.tar.xz \
    && rm -rf "$GNUPGHOME" python.tar.xz.asc \
    && mkdir -p /usr/src/python \
    && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
    && rm python.tar.xz \
    \
    && cd /usr/src/python \
    && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
    && ./configure \
        --build="$gnuArch" \
        --enable-loadable-sqlite-extensions \
        --enable-shared \
        --with-system-expat \
        --with-system-ffi \
        --without-ensurepip \
    && make -j "$(nproc)" \
    && make install \
    && ldconfig \
    \
    && apt-get purge -y --auto-remove $buildDeps \
    \
    && find /usr/local -depth \
        \( \
            \( -type d -a -name test -o -name tests \) \
            -o \
            \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        \) -exec rm -rf '{}' + \
    && rm -rf /usr/src/python
RUN cd /usr/local/bin \
    && ln -s idle3 idle \
    && ln -s pydoc3 pydoc \
    && ln -s python3 python \
    && ln -s python3-config python-config
RUN set -ex; \
    \
    wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
    \
    python get-pip.py \
        --disable-pip-version-check \
        --no-cache-dir \
        "pip==$PYTHON_PIP_VERSION" \
    ; \
    pip --version; \
    \
    find /usr/local -depth \
        \( \
            \( -type d -a -name test -o -name tests \) \
            -o \
            \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        \) -exec rm -rf '{}' +; \
    rm -f get-pip.py

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
ENV MONO_VERSION 5.4.1.6
RUN cd /tmp && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-official.list && \
    apt-get update && \
    apt-get install -y binutils mono-devel ca-certificates-mono fsharp mono-vbnc nuget referenceassemblies-pcl

# Install Javascript
ENV NODE_MAJOR 8
# npm 4.1.2 needed for Reason installation. Latest 5.3.0 doesn't work for some reason
ENV NPM_VERSION 4.1.2
RUN cd /tmp && \
    curl -sL https://deb.nodesource.com/setup_$NODE_MAJOR.x | bash - && \
    apt-get install nodejs -y && \
    npm install -g npm@$NPM_VERSION

# Install PHP
ENV PHP_VERSION 7.0
RUN cd /tmp && \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated php$PHP_VERSION

# Install D
ENV D_MAJOR 2.x
ENV D_VERSION 2.075.0
RUN cd /tmp && \
    apt-get install -y --no-install-recommends xdg-utils libcurl3 && \
    wget "http://downloads.dlang.org/releases/$D_MAJOR/$D_VERSION/dmd_$D_VERSION-0_amd64.deb" -O dmd_$D_VERSION-0_amd64.deb && \
    dpkg -i dmd_$D_VERSION-0_amd64.deb && \
    apt-get install -f -y && \
    rm dmd_$D_VERSION-0_amd64.deb

# Install Haskell (no easy way to install specific version)
RUN \
    apt-get install -y haskell-platform

# Install Ruby
ENV RB_MAJOR 2.4
ENV RB_VERSION 2.4.1
RUN cd /tmp && \
    wget "https://cache.ruby-lang.org/pub/ruby/$RB_MAJOR/ruby-$RB_VERSION.tar.gz" -O ruby-$RB_VERSION.tar.gz && \
    tar -xvzf ruby-*.tar.gz && \
    cd ruby-$RB_VERSION/ && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf ruby-$RB_VERSION.tar.gz ruby-$RB_VERSION/

# Install Scala
ENV SCALA_VERSION 2.12.0
ENV SCALA_HOME /usr/lib
RUN cd /tmp && \
    wget "http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz" -O scala-$SCALA_VERSION.tgz && \
    tar -xvzf scala-$SCALA_VERSION.tgz && \
    mv scala-$SCALA_VERSION/ $SCALA_HOME && \
    rm scala-$SCALA_VERSION.tgz
ENV PATH $SCALA_HOME/scala-$SCALA_VERSION/bin:$PATH

# Install Lua
ENV LUA_VERSION 2.0.4
RUN cd /tmp && \
    wget "http://luajit.org/download/LuaJIT-$LUA_VERSION.tar.gz" -O LuaJIT-$LUA_VERSION.tar.gz && \
    tar -xvf LuaJIT-$LUA_VERSION.tar.gz && \
    cd LuaJIT-$LUA_VERSION && \
    make && \
    make install && \
    cd .. && \
    rm -rf LuaJIT-$LUA_VERSION.tar.gz LuaJIT-$LUA_VERSION

# Install Perl
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

# Install OCaml
ENV OCAML_VERSION 4.04.1
RUN cd /tmp && \
    apt-get update && \
    apt-get install -y opam musl-dev && \
    wget 'https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh' -O - | sh -s /usr/local/bin && \
    opam init -a && \
    opam switch $OCAML_VERSION && \
    eval $(opam config env) && \
    opam update

# Install Kotlin
ENV KOTLIN_VERSION 1.1.2-2
ENV KOTLIN_HOME /usr/local/kotlin
RUN cd /tmp && \
    wget -k "https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip" && \
    unzip "kotlin-compiler-${KOTLIN_VERSION}.zip" && \
    mkdir -p "${KOTLIN_HOME}" && \
    mv "/tmp/kotlinc/bin" "/tmp/kotlinc/lib" "${KOTLIN_HOME}" && \
    rm ${KOTLIN_HOME}/bin/*.bat && \
    chmod +x ${KOTLIN_HOME}/bin/* && \
    ln -s "${KOTLIN_HOME}/bin/"* "/usr/bin/"

# Install Rust
ENV RUST_VERSION 1.18.0
ENV RUST_ARCHIVE rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz
ENV RUST_DOWNLOAD_URL https://static.rust-lang.org/dist/${RUST_ARCHIVE}
RUN mkdir -p /rust && \
    cd /rust && \
    curl -fsOSL $RUST_DOWNLOAD_URL && \
    curl -s $RUST_DOWNLOAD_URL.sha256 | sha256sum -c - && \
    tar -C /rust -xzf $RUST_ARCHIVE --strip-components=1 && \
    rm $RUST_ARCHIVE && \
    ./install.sh
ENV PATH $PATH:/root/.cargo/bin
# this part is for adding some (offline) packages
RUN cargo install cargo-local-registry
ENV USER root
RUN cd /tmp && \
    cargo new depdummy && \
    cd depdummy && \
    printf 'libc = "0.2.26"\nrand = "0.3.15"' >> Cargo.toml && \
    cargo build && \
    cargo local-registry --sync Cargo.lock /root/.cargo/bin && \
    printf "[source.crates-io]\nregistry = 'https://github.com/rust-lang/crates.io-index'\nreplace-with = 'local-registry'\n\n[source.local-registry]\nlocal-registry = '/root/.cargo/bin'" >> /root/.cargo/config && \
    cd /tmp && rm -rf depdummy

# Install Reason (opam required, see ocaml installation)
ENV REASON_VERSION 1.13.6
RUN npm install -g https://github.com/reasonml/reason-cli/archive/beta-v-$REASON_VERSION-bin-linux.tar.gz

# Install Elixir (doesn't seem to work anymore)
ENV ELIXIR_VERSION 1.2.6
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections  # See : https://github.com/phusion/baseimage-docker/issues/58
RUN echo "deb http://packages.erlang-solutions.com/ubuntu trusty contrib" >> /etc/apt/sources.list && \
    apt-key adv --fetch-keys http://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc && \
    apt-get -qq update && \
    apt-get install -y esl-erlang
RUN wget "https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb" && \
    dpkg -i erlang-solutions_1.0_all.deb && \
    rm erlang-solutions_1.0_all.deb && \
    apt-get update && \
    apt-get install -y elixir=$ELIXIR_VERSION*
RUN mix local.hex --force && \
    mix local.rebar --force

# Cleanup
RUN rm -rf /tmp/*
RUN apt-get autoremove -y
#RUN apt-get remove --purge -y wget make curl bzip2 unzip
RUN apt-get clean