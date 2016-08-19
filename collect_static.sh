#!/usr/bin/env bash
eval $(docker-machine env istebu-core01)
# docker-compose run app /usr/local/bin/python manage.py collectstatic --noinput
docker-compose run app /usr/local/bin/python manage.py collectstatic --noinput