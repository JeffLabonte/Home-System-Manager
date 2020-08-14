#!/bin/bash

DJANGO_SECRET_KEY='Update me'

DB_NAME='Update ME'

DB_HOST='localhost'
DB_PORT='5432'

DB_USER='Update ME'
DB_PASSWORD='Update ME'

sed -i "s/DATABASE_NAME/${DB_NAME}/g" docker-compose.yml
sed -i "s/DATABASE_HOST/${DB_HOST}/g" docker-compose.yml
sed -i "s/DATABASE_PORT/${DB_PORT}/g" docker-compose.yml
sed -i "s/DATABASE_USER/${DB_USER}/g" docker-compose.yml
sed -i "s/DATABASE_PASSWORD/${DB_PASSWORD}/g" docker-compose.yml

sed -i "s/SECRET_KEY$/${DJANGO_SECRET_KEY}/g" docker-compose.yml
