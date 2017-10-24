#!/usr/bin/env sh

# Find the main class
MAIN=`grep -lr --include '*.py' '__main__' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .py file. Looking for '__main__', but not found."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
