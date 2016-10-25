#!/usr/bin/env bash

# first cd into the directory that you have to copy to volume
# then give the foloowing command which copies the folder contents
# to the remote folder named ecommerceistebu_media-data
cd static_in_env/media_root
ls -la


docker-machine scp -r . istebu-core01:ecommerceistebu_media-data


# after that ssh into the machine
docker-machine ssh istebu-core01


# cd into the directory that we copied our local files:
cd ecommerceistebu_media-data


#Our data volume path is as follows, we gathered this by
#issuing the inspect command
#
#docker volume ls
#docker volume inspect ecommerceistebu_media-data
#
#/var/lib/docker/volumes/ecommerceistebu_media-data/_data/


# make superuser yourself:
sudo su


# After that issue the following command to copy the contents of
# current directory to the volume:
cp -r . /var/lib/docker/volumes/ecommerceistebu_media-data/_data/
