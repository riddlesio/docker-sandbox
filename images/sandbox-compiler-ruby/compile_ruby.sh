#!/usr/bin/env sh
set -e

MAIN=`find "$SOURCE_DIR" -name '*.rb' | xargs grep -lr '#!/usr/bin/env ruby'`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .rb file. Looking for '#!/usr/bin/env ruby', but not found. Add it to the first line of your main .rb file."
	exit 1
fi

cp -r $SOURCE_DIR/* "$BIN_DIR"
chmod -R +rx $BIN_DIR

MAIN=${MAIN##$SOURCE_DIR/}
echo "$MAIN" > "$BIN_DIR/manifest"
