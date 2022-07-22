# Postgres Database Server
-  `cd pg-database-server`
- Start docker shell `sh ./docker-shell.sh`
- Can exit the docker shell without shutting down by typing `ctrl+d`
- Can reconnect to docker shell by typing...
- Check migration status: `dbmate status`
- To shut down docker container, type `ctrl+c`

## Create a new migration script 
#### These would have no tables created, and will update the schema.sql

Examples:
`dbmate new base_tables`

`dbmate new seed_data`

## Running Migrations

`dbmate up` (see db/migrations for what tables are created)

`dbmate rollback`

`dbmate dump`

`dbmate status`