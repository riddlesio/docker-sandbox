#!/usr/bin/env sh
set -e

MAIN=`find "$SOURCE_DIR" -type f \( -iname \*.pl -o -iname \*.plx \) | xargs grep -lr '#!/usr/bin/env perl'`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .pl or .plx file. Looking for '#!/usr/bin/env perl', but not found. Add it to the first line of your main .pl or .plx file."
	exit 1
fi

cp -r $SOURCE_DIR/* "$BIN_DIR"
chmod -R +rx $BIN_DIR

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
