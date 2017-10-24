#!/usr/bin/env sh

# Find the main class
MAIN=`grep -lr --include '*.js' '__main__' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .js file. Looking for '__main__', but not found. Add it in a comment to your main .js file."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
