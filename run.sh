#!/bin/bash

export FLASK_ENV=development
export PYTHONPATH=$PWD
nohup celery -A swagger_server.background beat --loglevel=DEBUG > lottery_beat.txt

flask run
