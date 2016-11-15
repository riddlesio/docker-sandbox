FROM gcr.io/riddles-microservices/base:latest

# initialize package cache to be able to install packages
RUN \
    apt-get update && \
    apt-get -y install software-properties-common wget make curl bzip2

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
ENV JAVA_VERSION 8u91
RUN wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jdk-$JAVA_VERSION-linux-x64.tar.gz" && \
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
RUN \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list && \
    apt-get update && \
    apt-get -y install mono-mcs

## Install Javascript
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    apt-get install nodejs -y && \
    npm install -g npm@latest

## Install PHP
RUN \
    add-apt-repository -y ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y --allow-unauthenticated php5.6

## Install D
ENV D_MAJOR 2.x
ENV D_VERSION 2.071.0
RUN \
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
RUN \
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
RUN \
    wget "http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz" -O scala-$SCALA_VERSION.tgz && \
    tar -xvzf scala-$SCALA_VERSION.tgz && \
    mv scala-$SCALA_VERSION/ $SCALA_HOME && \
    rm scala-$SCALA_VERSION.tgz
ENV     PATH $SCALA_HOME/scala-$SCALA_VERSION/bin:$PATH

## Install Lua
ENV LUA_VERSION 2.0.4
RUN \
    wget "http://luajit.org/download/LuaJIT-$LUA_VERSION.tar.gz" -O LuaJIT-$LUA_VERSION.tar.gz && \
    tar -xvf LuaJIT-$LUA_VERSION.tar.gz && \
    cd LuaJIT-$LUA_VERSION && \
    make && \
    make install && \
    cd .. && \
    rm -rf LuaJIT-$LUA_VERSION.tar.gz LuaJIT-$LUA_VERSION

## Install Perl
ENV PERL_VERSION 5.24.0
RUN \
    curl -SL "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/perl-$PERL_VERSION.tar.bz2" -o perl-$PERL_VERSION.tar.bz2 && \
    tar -xjf perl-$PERL_VERSION.tar.bz2
RUN cd perl-$PERL_VERSION && \
    ./Configure -Duse64bitall -Duseshrplib -Dprefix=/usr -Dcc=gcc -des
RUN cd perl-$PERL_VERSION && \
    make && \
    make install && \
    rm /usr/bin/perl && \
    cp /usr/bin/perl$PERL_VERSION /usr/bin/perl
RUN rm -rf perl-$PERL_VERSION.tar.bz2 perl-$PERL_VERSION  # only works in separate RUN?

## Install Pascal
ENV PASCAL_VERSION 3.0.0
RUN \
    wget "ftp://freepascal.stack.nl/pub/fpc/dist/$PASCAL_VERSION/i386-linux/fpc-$PASCAL_VERSION.i386-linux.tar" -O fpc-$PASCAL_VERSION.i386-linux.tar && \
    tar -xvf fpc-$PASCAL_VERSION.i386-linux.tar && \
    cd fpc-$PASCAL_VERSION.i386-linux && \
    ./install.sh && \
    cd .. && \
    rm -rf fpc-$PASCAL_VERSION.i386-linux fpc-$PASCAL_VERSION.i386-linux.tar

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
RUN apt-get autoremove -y
#RUN apt-get remove --purge -y wget make curl bzip2
RUN apt-get clean