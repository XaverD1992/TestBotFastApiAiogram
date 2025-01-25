FROM python:3.11

RUN apt-get update && \
    pip install --no-cache-dir poetry

RUN mkdir /bot

RUN poetry config virtualenvs.create false

WORKDIR /bot

COPY pyproject.toml poetry.lock ./

RUN poetry install

#RUN pip3 install aiohttp
#RUN pip3 install python-dotenv
#RUN pip3 install aiogram

COPY ./ ./

#CMD ["python", "bot.py"]
CMD ["/bin/bash", "-c", "python bot.py"]