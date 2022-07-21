#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Define some environement variables
export IMAGE_NAME="mco-api-server"
export BASE_DIR=$(pwd)
export PERSISTENT_DIR=$(pwd)/../persistent-folder/

# Create the network if we don't have it yet
docker network inspect mco-network >/dev/null 2>&1 || docker network create mco-network

# Build the image based on the Dockerfile
docker build -t $IMAGE_NAME -f Dockerfile .

# Run the container
docker run --rm --name $IMAGE_NAME -ti \
--mount type=bind,source="$BASE_DIR",target=/app \
--mount type=bind,source="$PERSISTENT_DIR",target=/persistent-folder \
-p 9000:9000 \
-e DEV=1 \
-e DATABASE_URL=$DATABASE_URL \
--network mco-network $IMAGE_NAME