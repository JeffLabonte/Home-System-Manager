SHELL := /bin/bash

deps_prod:
	pip install -r requirements/requirements.txt

deps_dev:
	pip install -r requirements/requirements.dev.txt

deps_test:
	pip install -r requirements/requirements.test.txt

