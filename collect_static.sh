#!/usr/bin/env bash
eval $(docker-machine env default)
docker-compose run app /usr/local/bin/python manage.py collectstatic