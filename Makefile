default: test

black:
	poetry run black .

test:
	poetry run pydocstyle --match-dir='(?!tests).*' # Enforce codestyle, exclude tests directory
	poetry run pytest --cov=src/ tests              # Run tests and generate coverage report
