#!/usr/bin/env sh

MAIN=`grep -lr --include '*.pl' --include '*.plx' '#!/usr/bin/env perl' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .pl or .plx file. Looking for '#!/usr/bin/env perl', but not found. Add it to the first line of your main .pl or .plx file."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"