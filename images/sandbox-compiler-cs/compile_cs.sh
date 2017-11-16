#!/usr/bin/env sh
set -e

find "$SOURCE_DIR" -name '*.cs' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 mcs -out:"$BIN_DIR/run_ai"

if [ $? -gt 0 ]
then
	exit 1
fi

echo "run_ai" > "$BIN_DIR/manifest"
