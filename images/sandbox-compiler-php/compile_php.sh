#!/usr/bin/env sh
set -e

# Find the main class
MAIN=`find "$SOURCE_DIR" -name '*.php' | xargs grep -lr '__main__'`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .php file. Looking for '__main__', but not found. Add it in a comment to your main .php file."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
