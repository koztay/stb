#!/usr/bin/env bash

# set the nevironment for digital-ocean
#source ~/.bashrc
#dvm use 1.10.3
#docker -v
eval $(docker-machine env istebu-core01)
#
## Delete all containers (server client versiyon uyuşmazlığı yüzünden çalışmıyor.)
#docker rm -f $(docker ps -a -q)
## Delete all images
#docker rmi -f $(docker images -q)

# Build with no-cache
docker-compose -f docker-compose-production.yml build

# Up containers
docker-compose -f docker-compose-production.yml up -d

# Make migrations
#docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py makemigrations

# Migrate
#docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py migrate

# sonrasında bir daha collectstatic yapmak gerekebiliyor:
#docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py collectstatic --noinput