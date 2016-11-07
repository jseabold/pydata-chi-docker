#! /bin/bash

docker-compose -p dask-distributed up -d
docker-compose -p dask-distributed scale dask-worker=4
