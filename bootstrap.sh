#!/bin/bash

echo -e "Booting Kafka and Zookeeper"
docker-compose up -d 

echo -e "Sleeping 30 seconds"
sleep 30

echo -e "Running waiter database"
cd waiter
docker-compose up -d
cd ..

echo -e "Running cooker database"
cd cooker
docker-compose up -d
cd ..

echo -e "Running bartender database"
cd bartender
docker-compose up -d
cd ..