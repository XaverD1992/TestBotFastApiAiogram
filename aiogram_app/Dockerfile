FROM python:3.11

RUN pip install poetry

RUN mkdir /bot

WORKDIR /bot

COPY ../pyproject.toml ../poetry.lock ./

RUN poetry install --no-root

COPY ./ ./

CMD ["python", "bot.py"]