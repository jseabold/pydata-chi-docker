#! /bin/bash

docker-compose -p dask-distributed stop
docker-compose -p dask-distributed rm -f
