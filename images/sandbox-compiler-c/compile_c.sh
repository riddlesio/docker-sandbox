#!/usr/bin/env sh
set -e

# Pipe to xargs to escape possible spaces and other special characters in the file paths
find "$SOURCE_DIR" -name '*.c' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 gcc -std=c99 -static -Isrc -pthread -o "$BIN_DIR/run_ai" -O2 -lm

if [ $? -gt 0 ]
then
	exit 1
fi

chmod -R +rx $BIN_DIR

echo "run_ai" > "$BIN_DIR/manifest"
