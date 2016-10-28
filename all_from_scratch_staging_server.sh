#!/usr/bin/env bash

eval $(docker-machine env istebu-core01)
# eval $(docker-machine env istebu)
# Stop and remove all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Delete all images
docker rmi -f $(docker images -q)

# Delete all volumes
docker volume ls -qf dangling=true | xargs docker volume rm

# Build with no-cache
docker-compose -f docker-compose-production.yml build --no-cache

# Up containers
docker-compose -f docker-compose-production.yml up -d

#######
# Herşeyi sıfırsdan başlatınca öncelikle .env dosyasındaki verilerden database, user ve password
# oluşturuluyor. Ancak sonrasında migrate yapmak istendiğinde hata veriyor, çünkü auth user yok diyor.
# hata şöyle:
# django.db.utils.ProgrammingError: relation "auth_user" does not exist

# Bunun için önce aşağıdaki komutu veriyoruz:
# docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py migrate auth
# bu da aşağıdaki hatayı veriyor:
# psycopg2.ProgrammingError: relation "django_site" does not exist
# psycopg2.ProgrammingError: relation "django_site" does not exist
# LINE 1: SELECT (1) AS "a" FROM "django_site" LIMIT 1

# hata vermesi önemli değil en sonunda migrate komut verince sıkıntısız çalışıyor:
# docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py migrate

#    KEMALs-MacBook-Retina:ecommerce_istebu kemal$ docker-compose -f docker-compose-production.yml run app /usr/local/bin/python manage.py migrate
#    the fucking secret_key is: d!qmv1bs^e3)4(0p#=d=!gap^$b8vlm7*6=bfn&mgh^6p8@dpp
#    the fucking DEBUG setting is: True
#    Operations to perform:
#      Synchronize unmigrated apps: staticfiles, data_importer, tinymce, crispy_forms, messages, suit, django_filters
#      Apply all migrations: visual_site_elements, analytics, products, registration, contenttypes, carts, sessions, auth, static_pages, importer, sites, newsletter, admin, taggit, orders, blog
#    Synchronizing apps without migrations:
#      Creating tables...
#        Running deferred SQL...
#      Installing custom SQL...
#    Running migrations:
#      No migrations to apply.



