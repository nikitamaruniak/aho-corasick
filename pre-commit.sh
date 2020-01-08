#! /bin/sh

echo "Checking code style..."
black --check --diff .
if [ $? -ne 0 ]
then
  echo "Code style check failed."
  exit 1
else
  echo "Code syle check passed."
fi

echo "All checks passed."