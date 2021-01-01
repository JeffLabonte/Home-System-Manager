SHELL := /usr/bin/env bash

docker_compose_full_reset:
	docker-compose down -v
	docker-compose up -d

update_dev_configs:
	make reset_docker_compose
	./envs/env.dev

codestyle:
	flake8

start_server:
	docker-compose up -d

stop_server:
	docker-compose down

test_unit:
	cd src/ && py.test tests/unit/
