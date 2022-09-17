#!/bin/bash
docker build --no-cache -f Dockerfile -t uvicorn-fastapi:latest ../
#docker build -f Dockerfile -t uvicorn-fastapi:latest ../
#docker scan uvicorn-fastapi:latest
docker images uvicorn-fastapi:latest
