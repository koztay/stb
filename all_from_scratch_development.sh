#!/usr/bin/env bash

eval $(docker-machine env istebu)
# eval $(docker-machine env istebu)
# Stop and remove all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Delete all images // tüm imajları silmeye gerek yok ki postgres, redis vb. niye siliyorsun?
docker rmi -f $(docker images -q)

# Delete all volumes // volume 'ları da silmeye gerek olmayabilir.
docker volume ls -qf dangling=true | xargs docker volume rm

# Build with no-cache // no-cache yapmak lazım yalnız olmayınca olmuyor..
docker-compose -f docker-compose-development.yml build --no-cache

# Up containers
docker-compose -f docker-compose-development.yml up -d