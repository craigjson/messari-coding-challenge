# messari-coding-challenge

Implementation of RSS Feed scraper for Messari Back End role

# Quickstart

## Install Necessary Software

This project uses [Docker](https://docs.docker.com/get-docker/), it is neccesary to launch and run the system.

## Environment Variables

We use a `.env` file to inject environment variables into docker containers

In the top level directory, create a .env file and copy the sample vars below. if this were production, we would have multiple environment files e.g. `.env.dev` or `.env.prod`

1. `touch .env`
2. `REDIS_HOST="redis"`  
   `REDIS_PORT=6379`  
   `POSTGRES_CONNECTION_STRING="postgresql+psycopg2://postgres:postgres@db:5432"`

## Start the application

This application is configured to run within a handful of docker containers.

Start it by running  
`docker compose up`

Note: Due to the way that docker-compose depends-on works, which is to only wait for the starting of a service instead of it's start completion, it is possible that the Flask API will retry starting up if the DB is not yet finished booting.

# Environment Setup For Contributing

Note: Copy Environment variables from .vscode/launch.json as they are slightly different than the ones used for Docker.

This repository uses python venv for local development.

Create the virtual environment, activate it and install requirements.

1. `python3 -m venv venv`
2. `. venv/bin/activate`
3. `cd app`
4. `pip3 install -r requirements.txt`

Run the docker containers of neccessary depedencies, alternatively you could run postgres/redis locally.  
`docker compose up redis db`

Run the flask app to test changes, I like using the VSCode debugger to do this, but you can also do it in the CLI by runnng  
`flask --app app.py --debug run`
