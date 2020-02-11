install:
	@poetry install

lint:
	@poetry run flake8 gendiff

run_test:
	@poetry run pytest