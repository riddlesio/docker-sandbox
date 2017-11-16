#!/usr/bin/env sh
set -e

# Find the main class
MAIN=`find "$SOURCE_DIR" -name '*.js' | xargs grep -lr '__main__'`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .js file. Looking for '__main__', but not found. Add it in a comment to your main .js file."
	exit 1
fi

# look into bin_dir ownership because its a mount
rm -rf $BIN_DIR
mkdir -p $BIN_DIR
cp -r $SOURCE_DIR/* "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
