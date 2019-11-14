#version: ballerina-prime-testing:v2
#prime number: 100003
#sudo docker build -t anushiya/ballerina-prime-testing:v2 .
#sudo docker push anushiya/ballerina-prime-testing:v2
FROM ballerina/ballerina-runtime:0.991.0
COPY ballerina-prime.balx /home/ballerina
EXPOSE 8688 
EXPOSE 9797
CMD ballerina run --observe ballerina-prime.balx
