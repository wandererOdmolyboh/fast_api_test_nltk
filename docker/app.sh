#!/bin/bash

python tests/download_data.py

gunicorn src.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000