#version: ballerina-1.0.2-prime-testing:v2
#sudo docker build -t anushiya/ballerina-1.0.2-prime-testing:v2 .
#sudo docker push anushiya/ballerina-1.0.2-prime-testing:v2
# FROM openjdk:8-jre-alpine
FROM ballerina/ballerina:1.0.2

# ADD ballerina-prime-echo-alpha.jar ballerina-prime-echo-alpha.jar
COPY ballerina-prime-echo-alpha.jar ballerina-prime-echo-alpha.jar

# RUN chmod +x ballerina-prime-echo-alpha.jar
EXPOSE 8688 
EXPOSE 9797

CMD ballerina run ballerina-prime-echo-alpha.jar --b7a.observability.enabled=true