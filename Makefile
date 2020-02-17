install:
	@poetry install

lint:
	@poetry run flake8 gendiff --max-line-length 99

test:
	@poetry run pytest --cov=gendiff tests/ --cov-report xml