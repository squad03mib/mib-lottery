#
# Docker file for Message in a Bottle v1.0
#
FROM python:3.9
LABEL maintainer="squad_3"
LABEL version="1.0"
LABEL description="Message in a Bottle Lottery Microservice"

# creating the environment
COPY . /app
# setting the workdir
WORKDIR /app
RUN chmod +x celery.sh
# installing all requirements
RUN ["pip", "install", "-r", "requirements.prod.txt"]

# exposing the port
EXPOSE 5002/tcp
# Main command
CMD  ./celery.sh

