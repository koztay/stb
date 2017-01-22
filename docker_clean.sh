#!/usr/bin/env bash
# set the nevironment for digital-ocean

eval $(docker-machine env istebu)
# Stop and remove all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)