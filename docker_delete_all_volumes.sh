#!/bin/bash
eval $(docker-machine env default)
# Stop and remove all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker volume ls -qf dangling=true | xargs docker volume rm
