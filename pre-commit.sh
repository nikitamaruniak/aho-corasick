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

echo "Running unit tests..."
python -m doctest *.py **/*.py
if [ $? -ne 0 ]
then
  echo "Unit tests failed."
  exit 1
else
  echo "Unit tests passed."
fi

echo "Running acceptance tests..."
acceptance_tests/acceptance_tests.sh
if [ $? -ne 0 ]
then
  echo "Acceptance tests failed."
  exit 1
else
  echo "Acceptance tests passed."
fi

echo "All checks passed."