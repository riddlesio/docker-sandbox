#!/usr/bin/env sh
set -e

# Find Delphi or Lazarus project file
MAIN=`find "$SOURCE_DIR" \( -name '*.dpr' -o -name '*.lpr' \) -not -path "./__MACOSX/*" | head -n 1`

if [ -z "$MAIN" ]
then
	# Find main Pascal file
	MAIN=`find "$SOURCE_DIR" -type f \( -iname \*.p -o -iname \*.pp -o -iname \*.pas \) | xargs grep -lr '__main__'`

	if [ -z "$MAIN" ]
	then
		>&2 echo "Could not find Delphi/Lazarus project file or main .pas file. Either add a .dpr or .lpr file to your project, or add __main__ in a comment to your main .pas file."
		exit 1
	fi
fi

fpc -o"$BIN_DIR/run_ai" -XS -O2 -vz -Tlinux "$MAIN"

if [ $? -gt 0 ]
then
	exit 1
fi

chmod -R +rx $BIN_DIR

echo "run_ai" > "$BIN_DIR/manifest"
