.PHONY: install clean
.DELETE_ON_ERROR:

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info'  -exec rm -r {} +
	rm -rf build
	rm -rf dist

install:
	pip install --editable .
	pip install -r requirements-dev.txt

test:
	python setup.py test

build:
	python setup.py sdist bdist_wheel

build-exe:
	python cxfreeze_setup.py build

upload:
	twine upload dist/*
