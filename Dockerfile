FROM python:3.11

RUN apt-get update && \
    pip install --no-cache-dir poetry

RUN mkdir /wb

RUN poetry config virtualenvs.create false

WORKDIR /wb

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install

COPY ./ ./


RUN chmod a+x /wb/infra/*.sh
