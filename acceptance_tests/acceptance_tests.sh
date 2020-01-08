#! /bin/sh

pushd "$(dirname $0)/../" > /dev/null || exit 3

echo "Running acceptance test 1/1..."
python ahocorasick.py acceptance_tests/dictionary.txt acceptance_tests/text.txt \
  | diff - acceptance_tests/expected.txt

RESULT=$?

if [ $RESULT -eq 0 ]
then
  echo "Passed."
else
  echo "Failed. Review the difference between actual and expected outputs above."
fi

popd > /dev/null

exit $RESULT