#!/bin/bash

echo -e "Stoping last containers"
docker stop $(docker ps -aq)

echo -e "Removing containers"
docker rm $(docker ps -aq) 