#!/bin/bash
# Pull the image
docker pull docker.io/bitnami/zookeeper
docker pull docker.io/bitnami/kafka
# Create the network if it doesn't exists
docker network create --drive bridge testing || true
# Start the zookeper
docker run --rm --name kafka-zookeeper-testing --network testing -d \
  -p 2181:2181 -e "ALLOW_ANONYMOUS_LOGIN=yes" bitnami/zookeeper
# Start the broker
docker run --rm --name kafka-broker-testing --network testing -d \
  -p 9092:9092 -e "ALLOW_PLAINTEXT_LISTENER=yes" \
  -e "KAFKA_CFG_ZOOKEEPER_CONNECT=kafka-zookeeper-testing:2181" \
   bitnami/kafka
# To create a topic
docker run -it --rm --network testing \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=kafka-zookeeper-testing:2181 \
    bitnami/kafka:latest kafka-topics.sh --create --zookeeper \
    kafka-zookeeper-testing:2181 --topic Calculo --partitions 3 \
    --replication-factor 1
# To list the topics
docker run -it --rm --network testing \
    -e KAFKA_CFG_ZOOKEEPER_CONNECT=kafka-zookeeper-testing:2181 \
    bitnami/kafka:latest kafka-topics.sh --list --zookeeper \
    kafka-zookeeper-testing:2181
# To produce messages
docker run -it --rm --network testing \
  -e "KAFKA_CFG_ZOOKEEPER_CONNECT=kafka-zookeeper-testing:2181" \
  -e "ALLOW_PLAINTEXT_LISTENER=yes" bitnami/kafka \
  kafka-console-producer.sh --broker-list kafka-broker-testing:9092 \
  --topic Calculo
# To consume messages
docker run -it --rm --network testing \
  -e "KAFKA_CFG_ZOOKEEPER_CONNECT=kafka-zookeeper-testing:2181" \
  -e "ALLOW_PLAINTEXT_LISTENER=yes" bitnami/kafka \
  kafka-console-consumer.sh --bootstrap-server kafka-broker-testing:9092 \
  --topic Calculo --from-beginning