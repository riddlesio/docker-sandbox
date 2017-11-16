#!/usr/bin/env sh
set -e

CARGO=`find ${SOURCE_DIR} -name "Cargo.toml"`
if [ -z "$CARGO" ]
then
	>&2 echo "Could not find Cargo.toml. This compiler uses Cargo to compile Rust, so include the Cargo.toml file."
	exit 1
fi

(cd ${SOURCE_DIR};cargo build --release)

if [ $? -gt 0 ]
then
	exit 1
fi

# gets the name of the bot executable from the Cargo.toml file
EXE=`grep "name =" "$CARGO" | cut -d " " -f3`
EXE=`echo ${EXE} | sed 's/^"\(.*\)"$/\1/'`

FULLPATH=`find ${SOURCE_DIR} -name "$EXE"`
mv ${FULLPATH} ${BIN_DIR}

echo "$EXE" > "$BIN_DIR/manifest"
