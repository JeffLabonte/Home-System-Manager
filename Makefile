SHELL := /bin/bash

setup:
	cp envs/env.template.sh envs/env.dev
	chmod +x envs/env.dev

prepare_python_env:
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

run_server:
	./src/manage.py runserver

