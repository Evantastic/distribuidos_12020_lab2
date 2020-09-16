#!/bin/bash
# Build the image
docker build -t pipeline-calculo-estadisticas .
# Run the container
docker run --rm --name calculo-estadisticas -v $(pwd)/app:/app \
    -e "CASSANDRA_USER=cassandra" \
    -e "CASSANDRA_PASSWORD=cassandra" \
    -e "CASSANDRA_HOST=cassandra-testing" \
    -e "CASSANDRA_PORT=9042" \
    -e "CASSANDRA_KEYSPACE=pipeline" \
    -e "REDIS_HOST=" \
    -e "REDIS_PORT=" \
    -e "REDIS_DB=" \
    --network cassandra-testing pipeline-calculo-estadisticas python /app/main.py