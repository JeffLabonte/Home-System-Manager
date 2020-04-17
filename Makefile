SHELL := /bin/bash

export FLASK_APP=src/home_manager_app.py
export FLASK_ENV=development

init_dev:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pip install -r requirements.test.txt

init_test:
	pip install -r requirements.test.txt

run_server:
	flask run

run_functional_test:
	pytest src/tests/functional/