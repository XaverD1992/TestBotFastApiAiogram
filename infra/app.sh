#!/bin/bash

alembic upgrade head
uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000
#gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000