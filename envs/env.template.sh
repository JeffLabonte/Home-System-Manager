#!/bin/bash

SECRET_DJANGO_KEY='Update me'

DB_NAME='Update ME'

DB_HOST='localhost'
DB_PORT='5432'

DB_USER='Update ME'
DB_PASSWORD='Update ME'

sed -i "s/DB_NAME/${DB_NAME}/g" docker-compose.yml
sed -i "s/DB_HOST/${DB_HOST}/g" docker-compose.yml
sed -i "s/DB_PORT/${DB_PORT}/g" docker-compose.yml
sed -i "s/DB_USER/${DB_USER}/g" docker-compose.yml
sed -i "s/DB_PASSWORD/${DB_PASSWORD}/g" docker-compose.yml

sed -i "s/SECRET_DJANGO_KEY/${SECRET_DJANGO_KEY}" docker-compose.yml
