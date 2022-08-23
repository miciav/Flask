#!/bin/bash
docker build --no-cache -f Dockerfile-multibuild -t gunicorn-flask-alpine:latest ../
docker scan gunicorn-flask-alpine:latest
docker images gunicorn-flask-alpine:latest