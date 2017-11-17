#!/usr/bin/env sh
set -e

# Find the main class
MAIN=`find ${SOURCE_DIR} -name '*.java' -exec grep -lr 'public static void main' {} +`

if [ -z "$MAIN" ]
then
	>&2 echo "Could not find main .java file. Looking for 'public static void main', but not found."
	exit 1
fi

# compile

# Pipe to xargs to escape possible spaces and other special characters in the file paths
find ${SOURCE_DIR} -name '*.java' -not -path "$SOURCE_DIR/__MACOSX/*" -print0 | xargs -0 javac -sourcepath "$SOURCE_DIR" -d "$BIN_DIR"

if [ $? -gt 0 ]
then
	>&2 echo "Compile with javac failed. If the compiler can't find the main class: Make sure you upload your .zip file with the correct class structure, so only include folders that are actually packages. Don't put your sources in a folder and then zip the folder, but directly zip the sources."
	exit 1
fi

MAIN=${MAIN##${SOURCE_DIR}/}
MAIN=${MAIN%%.java}
CURRENT_DIR=`pwd`

# create executable jar
cd "$BIN_DIR"
echo "Main-Class: $MAIN" > jar_manifest
jar cfm run_ai.jar jar_manifest `find . -name '*.class' -not -path "./__MACOSX/*"`

if [ $? -gt 0 ]
then
	exit 1
fi

ls | grep -v *.jar | xargs rm -rf

cd "$CURRENT_DIR"

chmod -R +rx $BIN_DIR

echo "run_ai.jar" > "$BIN_DIR/manifest"
