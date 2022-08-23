#!/bin/bash
docker build --no-cache -f Dockerfile-multibuild -t gunicorn-flask-alpine:latest ../