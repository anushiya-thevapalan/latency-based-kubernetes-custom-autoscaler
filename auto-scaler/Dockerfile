#version - anushiya/auto-scaler:v1
#docker build --no-cache -t anushiya/auto-scaler:v1 .
#docker push anushiya/auto-scaler:v1
FROM python:3.5

LABEL maintainer="anushiya122@gmail.com"

RUN apt-get update && apt-get install python3-pip -y
RUN apt-get install curl -y
RUN pip3 install numpy requests

ADD bash /home/auto-scaler/bash
ADD python-helpers /home/auto-scaler/python-helpers

WORKDIR /home/auto-scaler/bash

RUN chmod +x start_autoscaler.sh

ENTRYPOINT [ "bash", "./start_autoscaler.sh" ]