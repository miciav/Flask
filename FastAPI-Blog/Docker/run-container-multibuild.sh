#!/bin/bash
docker run --name fastapi-app --rm -p 8000:80 uvicorn-fastapi-alpine:latest