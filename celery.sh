#!/bin/bash
nohup celery -A swagger_server.background beat --loglevel=INFO > lottery_beat.txt &
nohup celery -A swagger_server.background worker --loglevel=INFO > lottery_worker.txt &

gunicorn --config gunicorn.conf.py wsgi:app