FROM python:3.11

RUN pip install poetry

RUN mkdir /wb


WORKDIR /wb

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY ./fastapi_app ./alembic ./alembic.ini ./


CMD ["uvicorn", "fastapi_app.main:app", "--host", "0.0.0.0", "--reload" , "--port", "8000"]