#!/bin/bash
docker build --no-cache -f Dockerfile -t gunicorn-flask:latest ../
docker scan gunicorn-flask:latest
docker images gunicorn-flask:latest
