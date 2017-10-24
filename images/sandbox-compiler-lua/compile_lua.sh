#!/usr/bin/env sh

# Find the main class
MAIN=`grep -lr --include '*.lua' '#!/usr/bin/env lua' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .lua file. Looking for '#!/usr/bin/env lua', but not found. Add it to the first line of your main .lua file."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
