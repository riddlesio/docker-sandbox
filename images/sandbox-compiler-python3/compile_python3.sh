#!/usr/bin/env sh
set -e

# Find the main class
MAIN=`find "$SOURCE_DIR" -name '*.py' | xargs grep -lr '__main__'`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .py file. Looking for '__main__', but not found."
	exit 1
fi

cp -r $SOURCE_DIR/* "$BIN_DIR"
chmod -R +rx $BIN_DIR

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
