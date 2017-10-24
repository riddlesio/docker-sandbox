#!/usr/bin/env sh

rm -rf $BIN_DIR
mkdir $BIN_DIR

MAIN=`egrep -lr --include '*.hs' 'main=|main =' $SOURCE_DIR`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .hs file. Looking for 'main =', but not found."
	exit 1
fi

#ghc -O2 --make -static -optc-static -optl-static "$MAIN" -optl-pthread -o "$BIN_DIR/run_ai" -idir:"$SOURCE_DIR"
ghc -O2 --make "$MAIN" -optl-pthread -o "$BIN_DIR/run_ai" -idir:"$SOURCE_DIR"

if [ $? -gt 0 ]
then
	exit 1
fi

echo "run_ai" > "$BIN_DIR/manifest"
