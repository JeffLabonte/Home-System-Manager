SHELL := /bin/bash

setup_dev_env:
	@if [ ! -d .venv/ ]; then\
		python3 -m venv .venv;\
	fi
	source .venv/bin/activate
	make deps_dev

create_migration:
	./src/manage.py makemigrations

build_docker:
	docker build -t grimsleepless/home_manager -f Dockerfile .

apt_deps:
	sudo apt install -y pass python3-venv

deps_prod:
	make apt_deps
	pip install -r requirements/requirements.txt

deps_dev:
	make apt_deps
	pip install -r requirements/requirements.dev.txt

deps_test:
	make apt_deps
	pip install -r requirements/requirements.test.txt

edit_database:
	pass home_manager_db_password > .vault_password
	ansible-vault edit secrets/database_env.sh --vault-password-file .vault_password

run_server:
	python manage.py runserver

