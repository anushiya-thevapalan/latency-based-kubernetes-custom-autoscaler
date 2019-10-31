#version: ballerina-prime-testing:v1
FROM ballerina/ballerina-runtime:0.991.0
COPY ballerina-prime.balx /home/ballerina
EXPOSE 8688 
EXPOSE 9797
CMD ballerina run --observe ballerina-prime.balx
