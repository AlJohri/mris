.PHONY: install clean
.DELETE_ON_ERROR:

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info'  -exec rm -r {} +
	rm -rf build
	rm -rf dist

install:
	pip install --upgrade -q pipenv
	pipenv install
	pipenv run pip install -e .

test:
	pipenv run pytest

build:
	pipenv run python setup.py sdist bdist_wheel

build-exe:
	pipenv run python cxfreeze_setup.py build

upload:
	pipenv run twine upload dist/*
