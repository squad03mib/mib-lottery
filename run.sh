#!/bin/bash

export FLASK_ENV=testing
export PYTHONPATH=$PWD
nohup celery -A swagger_server.background beat --loglevel=INFO > lottery_beat.txt &
nohup celery -A swagger_server.background worker --loglevel=INFO > lottery_worker.txt &
flask run
