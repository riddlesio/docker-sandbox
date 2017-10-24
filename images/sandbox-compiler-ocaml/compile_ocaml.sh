#!/usr/bin/env sh

(cd ${SOURCE_DIR} && ocamlbuild -lib unix -build-dir ${BIN_DIR} main.native)

if [ $? -gt 0 ]
then
	exit 1
fi

echo "main.native" > "$BIN_DIR/manifest"
