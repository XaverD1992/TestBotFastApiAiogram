# API на FastAPI для сбора данных в локальную БД + бот на Aiogram отдающий данные


## Стек технологий
![Python](https://img.shields.io/badge/python-3.11-blue?style=for-the-badge)
![Fastapi](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/-Postgres-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Aiogram](https://img.shields.io/badge/-Aiogram-009639?style=for-the-badge&logo=nginx&logoColor=white)

## Начало работы

Эти инструкции позволят вам запустить копию проекта на вашем локальном компьютере для разработки и тестирования.

<details>
<summary><strong>Запуск с использованием Docker</strong></summary>

1. Склонировать репозиторий на локальный компьютер:
```
git clone -b develop git@github.com:Studio-Yandex-Practicum/TestBotFastApiAiogram.git
```
2. Перейти в папку infra:
```
cd TestBotFastApiAiogram/infra
```
3. Запустить контейнеры с помощью Docker Compose:
```
docker compose up --build
```
Теперь приложение должно быть доступно по адресу:

http://127.0.0.1:80

А документация доступна по адресу:

http://127.0.0.1:80/docs
</details>