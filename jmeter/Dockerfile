FROM anushiya/jmeter-plugins:v1

LABEL maintainer="anushiya122@gmail.com"

RUN apt-get update && apt-get install python3.5 -y
RUN apt-get install python-pip -y
RUN pip install numpy requests schedule objectpath

ADD bash /home/jmeter/bash
ADD jar /home/jmeter/jar
ADD jmx /home/jmeter/jmx
ADD python /home/jmeter/python

WORKDIR /home/jmeter/bash

RUN chmod +x *.sh