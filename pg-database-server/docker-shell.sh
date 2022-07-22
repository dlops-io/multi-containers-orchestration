#!/bin/bash

set -e

# Create the network if we don't have it yet
docker network inspect mco-network >/dev/null 2>&1 || docker network create mco-network

# Run Postgres DB
docker-compose run --rm --service-ports pg-mco-client
