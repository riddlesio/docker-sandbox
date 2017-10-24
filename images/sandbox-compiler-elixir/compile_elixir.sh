#!/usr/bin/env sh

rm -rf $BIN_DIR
mkdir $BIN_DIR

MAIN=`egrep -lr --include '*.ex' 'def main' "$SOURCE_DIR"`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .ex file. Looking for 'def main', but not found."
	exit 1
fi

# Edit/move main .ex file to execute
MODULE=`grep "defmodule" $MAIN | cut -d " " -f2`
MODULE=`echo $MODULE | sed 's/^"\(.*\)"$/\1/'`

grep -v "$MODULE.main(" $MAIN > temp && mv temp $MAIN
MAINFILE=${MAIN##$SOURCE_DIR/}
cp "$MAIN" "$BIN_DIR/$MAINFILE"
echo "$MODULE.main(\" \")" >> $BIN_DIR/$MAINFILE

# Compile
find "$SOURCE_DIR" -name '*.ex' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 elixirc -o "$BIN_DIR"

if [ $? -gt 0 ]
then
	exit 1
fi

echo "$MAINFILE" > "$BIN_DIR/manifest"
