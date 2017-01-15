#!/usr/bin/env bash
source ~/.bashrc

# DOTOKEN = 50984b95f9042ddc668fa34f32e91f51b4e8e6c68983e016ac6a7903968ca055

# docker-machine create --driver digitalocean --digitalocean-image coreos-stable --digitalocean-userdata core-os-cloud-config.yml --digitalocean-ssh-user core --digitalocean-size 512mb --digitalocean-region 'fra1' --digitalocean-ipv6 --digitalocean-private-networking --digitalocean-access-token $DOTOKEN istebu-core02

# It does not work
# docker-machine create --driver digitalocean --digitalocean-image ubuntu-16-10-x64 --digitalocean-size 512mb --digitalocean-region 'fra1' --digitalocean-ipv6 --digitalocean-private-networking --digitalocean-access-token 50984b95f9042ddc668fa34f32e91f51b4e8e6c68983e016ac6a7903968ca055 istebu-ubuntu

# It works
# docker-machine create --driver digitalocean --digitalocean-size 1gb --digitalocean-image ubuntu-16-10-x64 --digitalocean-access-token $DOTOKEN istebu-ubuntu03


# It does not work
# docker-machine create --driver digitalocean -digitalocean-image coreos-stable --digitalocean-userdata core-os-cloud-config2.yml --digitalocean-ssh-user core --digitalocean-access-token $DOTOKEN istebu-core01

# create linode mavhines :
# docker-machine create -d generic --generic-ip-address {ip-address} --generic-ssh-key {private-key} --generic-ssh-user {username} --generic-ssh-port {ssh-port} {docker-vm-name}
docker-machine create -d generic --generic-ip-address 139.162.164.170 --generic-ssh-key ~/.ssh/id_rsa --generic-ssh-user dockeradmin linode-debian7