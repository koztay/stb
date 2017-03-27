#!/usr/bin/env bash
source ~/.bashrc

# DOTOKEN = 50984b95f9042ddc668fa34f32e91f51b4e8e6c68983e016ac6a7903968ca055

docker-machine create --driver digitalocean --digitalocean-image coreos-stable --digitalocean-userdata core-os-cloud-config.yml --digitalocean-ssh-user core --digitalocean-size 512mb --digitalocean-region 'fra1' --digitalocean-ipv6 --digitalocean-private-networking --digitalocean-access-token $DOTOKEN consulta-core01
# yukarıdaki komut aşağıdaki versiyonlara sahip DockerToolbox-1.13.0.pkg dosyasını kurduktan sonra çalıştı.
# 1.12.5 - 1.12.6 versiyonlarında çalışmıyordu... CoreOS machine yaratamıyordu. Hatta OS belirtilen hiçbit komutta
# provisioning yapamıyordu. Artık yeni versiyon mu düzeltti durumu, yoksa digitalocean mı bilmiyorum.
# detay versiyonlar şöyle :
# docker-machine : docker-machine version 0.9.0, build 15fd4c7
# docker : Docker version 1.13.0, build 49bf474
# docker-compose : docker-compose version 1.10.0, build 4bd6f1a



# It does not work
# docker-machine create --driver digitalocean --digitalocean-image ubuntu-16-10-x64 --digitalocean-size 512mb --digitalocean-region 'fra1' --digitalocean-ipv6 --digitalocean-private-networking --digitalocean-access-token 50984b95f9042ddc668fa34f32e91f51b4e8e6c68983e016ac6a7903968ca055 istebu-ubuntu

# It works
# docker-machine create --driver digitalocean --digitalocean-size 1gb --digitalocean-image ubuntu-16-10-x64 --digitalocean-access-token $DOTOKEN istebu-ubuntu03


# It does not work
# docker-machine create --driver digitalocean -digitalocean-image coreos-stable --digitalocean-userdata core-os-cloud-config2.yml --digitalocean-ssh-user core --digitalocean-access-token $DOTOKEN istebu-core01

# create linode mavhines :
# docker-machine create -d generic --generic-ip-address {ip-address} --generic-ssh-key {private-key} --generic-ssh-user {username} --generic-ssh-port {ssh-port} {docker-vm-name}
#docker-machine create -d generic --generic-ip-address 139.162.164.170 --generic-ssh-key ~/.ssh/id_rsa --generic-ssh-user dockeradmin linode-debian7