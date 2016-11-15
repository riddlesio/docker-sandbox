FROM    phusion/baseimage:0.9.19

# Necessary flags so apt-install is not going to complain
# about not being able to use interactive prompts
ENV     DEBIAN_FRONTEND noninteractive
ENV     TERM=linux

# initialize package cache to be able to install packages
RUN     apt-get update && \
        apt-get -y install apt-utils

RUN     mkdir /riddles
RUN     mkdir -p /var/log/riddles

# Locale should be the same in all containers
# Otherwise we'll get unicode errors when executing sandboxed commands
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8