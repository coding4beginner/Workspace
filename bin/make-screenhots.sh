<<<<<<< HEAD
#!/usr/local/bin/bash

THIS="$0"
[[ "$THIS" == "-bash" ]] && THIS="$1"

BASE="$(readlink -f "$THIS")"
BASE="$(dirname "$BASE")"

echo BASE=$BASE

=======
>>>>>>> a923a69 (-)
find . -name *.html 				|\
grep -v node_modules 				|\
while read FILE
do
<<<<<<< HEAD
	SHOT="${FILE/.html/.png}"
	SHOT="${SHOT/solution/exercise}"

	FLDR="${SHOT%/*}"
	SHOT="${FLDR}/SOLUTION.png"

	echo "$FILE -> $SHOT"

	node $BASE/screenshot.js  "$FILE" "$SHOT"
=======
	SHOT=${FILE/.html/.png};
	SHOT=${SHOT/solution/exercise};

	echo "$FILE -> $SHOT"

	node screenshot.js  $FILE $SHOT
>>>>>>> a923a69 (-)
done

