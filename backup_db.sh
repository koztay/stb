#!/usr/bin/env bash

if [ -z $1 ]; then
    echo "No docker-machine provided. Usage: $0 istebu-core01"
    exit 1
fi


eval $(docker-machine env $1)
source ~/.bashrc
dvm use 1.10.3

#NOW=$(date +"%Y%m%dT%H%M%SZ")
#DUMP_FILENAME="$NOW"_istebu_db.sql
##docker exec -t ecommerceistebu_postgres_1 pg_dumpall -c -U istebupostgr > $DUMP_FILENAME
#docker exec -t ecommerceistebu_postgres_1 pg_dump -c -U istebupostgr istebupgdb  > $DUMP_FILENAME

NOW=$(date +"%Y%m%dT%H%M%SZ")
DUMP_FILENAME="$NOW"_istebu_db_pgdumpall.sql
DUMP_FILENAME2="$NOW"_istebu_db_pgdump.sql
echo "step_1"
docker exec -it ecommerceistebu_postgres_1 sh -c 'PGPASSWORD=$POSTGRES_PASSWORD pg_dumpall -U $POSTGRES_USER -h localhost -p 5432 --clean --file='$DUMP_FILENAME''
docker exec -it ecommerceistebu_postgres_1 sh -c 'pg_dump -U $POSTGRES_USER $POSTGRES_DB > '$DUMP_FILENAME2''
echo "step_2"
docker cp ecommerceistebu_postgres_1:$DUMP_FILENAME .
docker cp ecommerceistebu_postgres_1:$DUMP_FILENAME2 .
echo "step_3"
docker exec -it ecommerceistebu_postgres_1 rm $DUMP_FILENAME
echo "step_4"
echo $DUMP_FILENAME