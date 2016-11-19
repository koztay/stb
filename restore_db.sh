#!/usr/bin/env bash

if [ -z $1 ]; then
    echo "No docker-machine provided. Usage: $0 istebu-core01"
    exit 1
fi

eval $(docker-machine env $1)
source ~/.bashrc
dvm use 1.10.3

#cat 20161115T201629Z_istebu_db.sql | docker exec -i ecommerceistebu_postgres_1 psql -U istebupostgr istebupgdb


if [ -z $2 ]; then
    echo "No dump provided. Usage: $0 201..._lesspass_db.sql"
    exit 1
fi

DUMP_FILENAME=$1

docker cp $DUMP_FILENAME ecommerceistebu_postgres_1:$DUMP_FILENAME
echo "step 1"
docker exec -it ecommerceistebu_postgres_1 sh -c 'PGPASSWORD=$POSTGRES_PASSWORD dropdb -U $POSTGRES_USER $POSTGRES_DB'
echo "step 2"
docker exec -it ecommerceistebu_postgres_1 sh -c 'PGPASSWORD=$POSTGRES_PASSWORD createdb -U $POSTGRES_USER $POSTGRES_DB'
echo "step 3"
docker exec -it ecommerceistebu_postgres_1 sh -c 'PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER $POSTGRES_DB -h localhost -p 5432 < '$DUMP_FILENAME''
echo "step 4"
docker exec -it ecommerceistebu_postgres_1 rm $DUMP_FILENAME