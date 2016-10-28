#!/usr/bin/env bash
source ~/.bashrc
docker-machine create --driver digitalocean --digitalocean-image coreos-stable --digitalocean-userdata core-os-cloud-config.yml --digitalocean-ssh-user core --digitalocean-size 512mb --digitalocean-region 'fra1' --digitalocean-ipv6 --digitalocean-private-networking --digitalocean-access-token $DOTOKEN istebu-staging-xubuntu
