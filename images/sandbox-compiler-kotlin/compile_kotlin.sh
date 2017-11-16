#!/usr/bin/env sh
set -e

# Pipe to xargs to escape possible spaces and other special characters in the file paths
find "$SOURCE_DIR" -name '*.kt' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 kotlinc -include-runtime -d ${BIN_DIR}/run_ai.jar

if [ $? -gt 0 ]
then
	exit 1
fi

echo "run_ai.jar" > "$BIN_DIR/manifest"
