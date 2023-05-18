# Getting started
```bash
    cp .env.example .env
    pip3 install -r requirements.txt
    make build
    make start
```
Also, you need to remember, that alembic.ini on the line 63 has the line with db connection for migrations and if you change some, don't forget to change it:
```bash
    sqlalchemy.url = postgresql://core_db_user:pLabn_42c@db:5432/core_db
```
And finally migrate it meanwhile Docker containers are on:
```bash
    make migrate
```
## Port is 8008

# Alembic migrations
Alembic should be inited when you first time use it (here is already initiated):
```bash
    alembic init alembic
```
To create alter migration:
```bash
    alembic revision -m "alter <table_name> table"
```
To run migration (should be run from inside the container, please, check Makefile for example):
```bash
    alembic upgrade head
```

# Purpose
For education, working solutions, etc. Use wherever you want and need. Please, share with somebody, who start to learn programming, it will help them.
If you'll find some issues or solutions, please - feel free to contribute.
### Let's leave this world better than we found it.
