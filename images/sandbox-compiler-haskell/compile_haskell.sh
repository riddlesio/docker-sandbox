#!/usr/bin/env sh
set -e

MAIN=`find "$SOURCE_DIR" -name '*.hs' | xargs grep -Elr 'main=|main ='`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .hs file. Looking for 'main =', but not found."
	exit 1
fi

#ghc -O2 --make -static -optc-static -optl-static "$MAIN" -optl-pthread -o "$BIN_DIR/run_ai" -idir:"$SOURCE_DIR"
ghc -O2 --make "$MAIN" -optl-pthread -o "$BIN_DIR/run_ai" -odir:"$BIN_DIR" -idir:"$SOURCE_DIR" -hidir:"$HI_DIR"

if [ $? -gt 0 ]
then
	exit 1
fi

chmod -R +rx $BIN_DIR

echo "run_ai" > "$BIN_DIR/manifest"
