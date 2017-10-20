FROM python:3.6.3-alpine3.6

ENV SETUPTOOLS_VERSION="36.6.0"
ENV NUMPY_VERSION="1.13.3"

RUN \
    apk --no-cache add musl-dev linux-headers g++ && \
    pip install -U "setuptools==${SETUPTOOLS_VERSION}" && \
    pip install "numpy==${NUMPY_VERSION}" && \
    apk del musl-dev linux-headers g++
