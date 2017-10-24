#!/usr/bin/env sh

MAIN=`grep -lr --include '*.rb' '#!/usr/bin/env ruby' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .rb file. Looking for '#!/usr/bin/env ruby', but not found. Add it to the first line of your main .rb file."
	exit 1
fi

rm -rf "$BIN_DIR"
cp -r "$SOURCE_DIR" "$BIN_DIR"

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
