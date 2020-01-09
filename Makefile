.PHONY: check_format format unit_tests acceptance_tests test

test: check_format unit_tests acceptance_tests

check_format:
	black --check --diff .

format:
	black .

unit_tests:
	python -m doctest *.py **/*.py

acceptance_tests:
	acceptance_tests/acceptance_tests.sh
