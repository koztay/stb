#!/usr/bin/env bash
eval $(docker-machine env istebu)
docker-compose run web /usr/local/bin/python manage.py migrate
