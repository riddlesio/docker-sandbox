#!/usr/bin/env sh
set -e

find "$SOURCE_DIR" -name '*.go' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 go build -o "$BIN_DIR/run_ai"

if [ $? -gt 0 ]
then
	exit 1
fi

echo "run_ai" > "$BIN_DIR/manifest"
