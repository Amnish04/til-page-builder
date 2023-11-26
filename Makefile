install:
	pip install -r requirements.txt

format:
	black .

lint:
	pylint src/til_page_builder tests/ integration/

test:
	pytest

run-failed-tests:
	pytest --last-failed 

test-watch:
	ptw

coverage:
	pytest --cov=src