#
# Docker file for Message in a Bottle v1.0
#
FROM python:3.9
LABEL maintainer="squad_3"
LABEL version="1.0"
LABEL description="Message in a Bottle Lottery Microservice"

# creating the environment
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY requirements.prod.txt /usr/src/app/

# installing all requirements
RUN ["pip", "install", "-r", "requirements.prod.txt"]

COPY . /usr/src/app

# exposing the port
EXPOSE 5002/tcp

# Main command
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
