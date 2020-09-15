SHELL := /bin/bash

deps_dev:
	pip install -r requirements/requirements.dev.txt

setup:
	cp templates/env.template.sh envs/env.dev
	chmod +x envs/env.dev
	make reset_docker_compose
	@echo "Run ./env/env.dev once you have set your variables"

docker_compose_full_reset:
	docker-compose down -v
	make update_dev_configs
	docker-compose up -d

enter_dev_env:
	docker-compose run web /bin/bash

update_dev_configs:
	make reset_docker_compose
	./envs/env.dev

reset_docker_compose:
	cp templates/docker-compose.template.yml docker-compose.yml

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

solus_deps:
	sudo eopkg it password-store python3

deps_prod:
	pip install -r requirements/requirements.txt

deps_test:
	pip install -r requirements/requirements.test.txt

run_server:
	./src/manage.py runserver

codestyle:
	flake8
