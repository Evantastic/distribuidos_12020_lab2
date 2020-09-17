#!/bin/bash
# Pull the image
docker pull redis:alpine
# Create the network if it doesn't exists
docker network create --driver bridge testing || true
# Start the container
docker run --rm --name redis-testing --network testing -d \
  -p 6379:6379 -v $(pwd)/data:/data -e "REDIS_PASSWORD=redis" \
  redis:alpine /bin/sh -c  'redis-server --appendonly yes \
  --requirepass ${REDIS_PASSWORD}' 
# To connect to redis through redis-cli
docker run -it --network testing --rm redis:alpine redis-cli -h redis-testing