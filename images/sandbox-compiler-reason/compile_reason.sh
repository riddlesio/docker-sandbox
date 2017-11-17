#!/usr/bin/env sh
set -e

(cd ${SOURCE_DIR} && rebuild -lib unix -build-dir ${BIN_DIR} main.native)

if [ $? -gt 0 ]
then
	exit 1
fi

chmod -R +rx $BIN_DIR

echo "main.native" > "$BIN_DIR/manifest"
