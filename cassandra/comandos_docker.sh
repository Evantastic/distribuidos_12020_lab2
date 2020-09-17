#!/bin/bash
# Pull the image
docker pull cassandra:3
# Create the network if it doesn't exists
docker network create --driver bridge testing || true
# Build the image
docker build -t pipeline-cassandra .
# Start the container
docker run --rm --name cassandra-testing --network testing -d \
  -p 7000:7000 -p 9042:9042 -v $(pwd)/db-data:/var/lib/cassandra \
  pipeline-cassandra
# To connect to cassandra through cqlsh
docker run -it --network testing --rm cassandra:3 \
  cqlsh -u cassandra -p cassandra cassandra-testing
