#!/bin/bash
docker run --name flask-app --rm -p 5000:80 gunicorn-flask:latest