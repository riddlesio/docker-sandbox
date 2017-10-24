#!/usr/bin/env sh

# Find the main class
MAIN=`grep -lr --include '*.scala' 'def main' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .scala file. Looking for 'def main', but not found."
	exit 1
fi

find "$SOURCE_DIR" -name '*.scala' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 scalac -sourcepath "$SOURCE_DIR" -d "$BIN_DIR/run_ai.jar"

if [ $? -gt 0 ]
then
	exit 1
fi

echo "run_ai.jar" > "$BIN_DIR/manifest"
