FROM python:3.10.0-slim

RUN apt update && apt -y upgrade && apt install -y gunicorn3
WORKDIR /code

COPY ../requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system app


COPY ../app /code/app
WORKDIR /code/app
CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:80", "main:app"]