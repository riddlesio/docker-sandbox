#!/usr/bin/env sh
set -e

# Find the main class
MAIN=`find "$SOURCE_DIR" -name '*.lua' | xargs grep -lr '#!/usr/bin/env lua'`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .lua file. Looking for '#!/usr/bin/env lua', but not found. Add it to the first line of your main .lua file."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
