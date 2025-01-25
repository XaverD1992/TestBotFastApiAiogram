FROM python:3.11

RUN apt-get update && \
    pip install --no-cache-dir poetry

RUN mkdir /bot

RUN poetry config virtualenvs.create false

WORKDIR /bot

COPY pyproject.toml poetry.lock ./

RUN poetry install


COPY ./ ./

CMD ["/bin/bash", "-c", "python bot.py"]