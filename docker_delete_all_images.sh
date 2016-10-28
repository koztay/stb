#!/usr/bin/env bash
eval $(docker-machine env istebu-core01)

# Delete all containers
docker rm -f $(docker ps -a -q)
# Delete all images
docker rmi -f $(docker images -q)