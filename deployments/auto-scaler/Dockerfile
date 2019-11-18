FROM ubuntu:18.04

RUN apt-get update && apt-get install python3.6 -y

RUN apt-get install nano
RUN apt-get install python3-pip -y
RUN pip3 install numpy
RUN pip3 install requests

RUN pwd

COPY /home/anushiyat/Documents/wso2/project/latency-based-kubernetes-custom-autoscaler /home/auto-scaler

CMD [ "executable" ]