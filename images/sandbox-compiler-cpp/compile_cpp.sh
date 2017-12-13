#!/usr/bin/env sh
set -e

find "$SOURCE_DIR" \( -name '*.cc' -o -name '*.cpp' \) -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 g++ -std=c++1y -static -Isrc -pthread -o "$BIN_DIR/run_ai" -O2 -lm

if [ $? -gt 0 ]
then
	exit 1
fi

chmod -R +rx $BIN_DIR

echo "run_ai" > "$BIN_DIR/manifest"
