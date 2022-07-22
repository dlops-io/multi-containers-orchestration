#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Define some environement variables
export IMAGE_NAME="mco-api-server"
export BASE_DIR=$(pwd)
export COMMON_DIR=$(dirname "$(pwd)")/common
export PERSISTENT_DIR=$(pwd)/../persistent-folder/
export DATABASE_URL="postgres://test:welcome123@pg-mco-server:5432/pg-mco"
export REDIS_URL="redis://mco-redis:6379/0"

# Create the network if we don't have it yet
docker network inspect mco-network >/dev/null 2>&1 || docker network create mco-network

# Build the image based on the Dockerfile
docker build -t $IMAGE_NAME -f Dockerfile .

# Run the container
docker run --rm --name $IMAGE_NAME -ti \
--mount type=bind,source="$BASE_DIR",target=/app \
--mount type=bind,source="$COMMON_DIR/dataaccess",target=/app/dataaccess \
--mount type=bind,source="$COMMON_DIR/datacollector",target=/app/datacollector \
--mount type=bind,source="$COMMON_DIR/auth",target=/app/auth \
--mount type=bind,source="$COMMON_DIR/taskqueue",target=/app/taskqueue \
--mount type=bind,source="$PERSISTENT_DIR",target=/persistent-folder \
-p 9000:9000 \
-e DEV=1 \
-e DATABASE_URL=$DATABASE_URL \
-e REDIS_URL=$REDIS_URL \
--network mco-network $IMAGE_NAME