#!/bin/bash
docker run --name fastapi-app --rm -p 5000:80 uvicorn-fastapi:latest