SHELL := /bin/bash

setup_dev_env:
	sudo apt install pass python3-venv
	@if [ ! -d .venv/ ]; then\
		python3 -m venv .venv;\
	fi
	source .venv/bin/activate
	make deps_dev

create_migration:
	./manage.py makemigrations

deps_prod:
	pip install -r requirements/requirements.txt

deps_dev:
	pip install -r requirements/requirements.dev.txt

deps_test:
	pip install -r requirements/requirements.test.txt

edit_database:
	pass home_manager_db_password > .vault_password
	ansible-vault edit secrets/database_env.sh --vault-password-file .vault_password

run_server:
	python manage.py runserver

