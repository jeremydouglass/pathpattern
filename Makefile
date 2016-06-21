init:
	pip install -r requirements.txt

test:
	python -m tests.tests

test_app:
	python -m tests.app