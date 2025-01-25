FROM python:3.11

RUN apt-get update && \
    pip install --no-cache-dir poetry

RUN mkdir /wb

RUN poetry config virtualenvs.create false

WORKDIR /wb

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install

#RUN pip3 install fastapi uvicorn apscheduler redis

#COPY ./fastapi_app ./alembic ./alembic.ini  ./

COPY ./ ./

#COPY ./infra .

RUN chmod a+x /wb/infra/*.sh

#CMD ["uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--reload" , "--port", "80"]