.PHONY: setup

setup:
	pip install -r requirements.txt

lint:
	pylint css_class_names.py tests/

test:
	nosetests
