#!/usr/bin/env bash

# set the nevironment for digital-ocean
#source ~/.bashrc
#dvm use 1.10.3
#docker -v
eval $(docker-machine env istebu)
#eval $(docker-machine env istebu)
#
## Delete all containers (server client versiyon uyuşmazlığı yüzünden çalışmıyor.)
#docker rm -f $(docker ps -a -q)
## Delete all images
#docker rmi -f $(docker images -q)

# Build with no-cache
docker-compose -f docker-compose-local-server.yml build

# Up containers
docker-compose -f docker-compose-local-server.yml up -d

# Make migrations
# docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py makemigrations
# yukarıdaki metodu kullanırsan ilave olarak container yaratıyor kullanma bunun yerine docker-machine ile ssh yap.
# sonrasında da aşağıdaki komutları ver
# docker ps (django app 'in id sini al.)
# docker exec it <django app id> bash (django app içerisinde bash komutu  verebiliriz artık.)
# python manage.py makemigrations
# python manage.py migrate.


# Migrate
#docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py migrate

# sonrasında bir daha collectstatic yapmak gerekebiliyor:
#docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py collectstatic --noinput