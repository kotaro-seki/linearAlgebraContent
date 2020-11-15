#!/bin/bash

# setup docker container from customed image
docker-compose up --no-recreate
# login
docker exec -it linear-algebra-content /bin/bash
