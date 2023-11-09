install:
	pip install -r requirements.txt

format:
	black .

lint:
	pylint src/

test:
	pytest

run-failed-tests:
	pytest --last-failed 

test-watch:
	ptw

coverage:
	pytest --cov=src