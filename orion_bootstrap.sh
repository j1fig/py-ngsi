#! /bin/bash

mkdir orion_build
cd orion_build

git clone git@github.com:whitesmith/fiware-orion-deps-docker.git
cd fiware-orion-deps-docker
docker build -t whitesmith/fiware-orion-deps:latest .
cd ..

git clone git@github.com:whitesmith/fiware-orion-docker.git
cd fiware-orion-docker
docker build -t whitesmith/fiware-orion:latest .
docker-compose up
