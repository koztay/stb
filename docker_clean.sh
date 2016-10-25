#!/usr/bin/env bash
# set the nevironment for digital-ocean
source ~/.bashrc
dvm use 1.10.3
docker -v
eval $(docker-machine env istebu-core01)
# Stop and remove all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)