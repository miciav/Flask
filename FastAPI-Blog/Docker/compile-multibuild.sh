#!/bin/bash
docker build --no-cache -f Dockerfile-multibuild -t uvicorn-fastapi-alpine:latest ../
#docker build -f Dockerfile-multibuild -t uvicorn-fastapi-alpine:latest ../
#docker scan gunicorn-flask-alpine:latest
docker images gunicorn-flask-alpine:latest