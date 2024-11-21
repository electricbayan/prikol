#!/bin/bash

gunicorn app:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8080