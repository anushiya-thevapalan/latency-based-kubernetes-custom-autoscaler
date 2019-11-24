#version - anushiya/monitoring-server:v1
#docker build --no-cache -t anushiya/monitoring-server:v1 .
#docker push anushiya/monitoring-server:v1
FROM python:3.6

ADD bash /home/monitoring-server/bash
ADD python /home/monitoring-server/python

RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install numpy flask requests

WORKDIR /home/monitoring-server/bash

RUN chmod +x start_monitoring_server.sh get_endpoints.sh

ENTRYPOINT [ "bash", "./start_monitoring_server.sh" ]