#!/usr/bin/env bash
eval $(docker-machine env istebu-core01)
# docker-compose run app /usr/local/bin/python manage.py collectstatic --noinput
docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py collectstatic --noinput