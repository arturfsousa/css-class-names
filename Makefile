.PHONY: setup lint test test-watch

setup:
	pip install -r requirements.txt

lint:
	pylint css_class_names.py tests/

test:
	nosetests --rednose

watch:
	nosetests --rednose --with-watch

coverage:
	nosetests --rednose --with-coverage
