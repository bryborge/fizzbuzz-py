.PHONY: venv install pre-commit clean

VERSION_FILE := .python-version
PY_VERSION := $(shell cat ${VERSION_FILE})

default: test

# SETUP / TEAR DOWN ENVIRONMENT ###############################################

setup: venv install pre-commit

venv:
	@echo "*** Creating .venv ..."
	poetry env use $(PY_VERSION)
	@echo "\n"

install:
	@echo "*** Installing dependencies ..."
	poetry install --no-root --sync

pre-commit:
	@echo "*** Setting up pre-commit ..."
	poetry run pre-commit install
	poetry run pre-commit autoupdate

clean:
	@echo "*** Clean environment ..."
	if [ -d .git/hooks ]; then rm -r .git/hooks; fi
	if [ -f poetry.lock ]; then rm poetry.lock; fi

# TESTING / FORMATTING ########################################################

format:
	poetry run pydocstyle --match-dir='(?!tests).*' # Enforce codestyle, exclude tests directory
	poetry run black .                              # Enforce PEP 8 coding style

test:
	poetry run pytest --cov=src/ tests # Run tests and generate coverage report
