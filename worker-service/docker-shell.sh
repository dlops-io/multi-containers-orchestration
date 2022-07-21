#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Define some environement variables
export IMAGE_NAME="mco-worker-service"
export BASE_DIR=$(pwd)
export COMMON_DIR=$(dirname "$(pwd)")/common
export DATABASE_URL=""
export REDIS_URL="redis://mco-redis:6379/0"

# Create the network if we don't have it yet
docker network inspect mco-network >/dev/null 2>&1 || docker network create mco-network

# Build Image
docker build -t $IMAGE_NAME -f Dockerfile .

# Run Container
docker-compose run --rm \
--volume "$BASE_DIR":/app \
--volume "$COMMON_DIR/dataaccess":/app/dataaccess \
--volume "$COMMON_DIR/datacollector":/app/datacollector \
--volume "$COMMON_DIR/datacollector":/app/auth \
-e MODE=dev \
-e DATABASE_URL=$DATABASE_URL \
-e REDIS_URL=$REDIS_URL \
--service-ports $IMAGE_NAME