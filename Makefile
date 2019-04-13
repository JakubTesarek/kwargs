all:
	@echo 'make clean | build | test'

clean:
	rm -rf *.pyc __pycache__
	rm -rf kwargs.egg-info build dist

build:
	python setup.py sdist bdist_wheel

test:
	python -m pytest
