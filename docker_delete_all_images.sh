#!/usr/bin/env bash
eval $(docker-machine env default)
docker rmi -f $(docker images -q)