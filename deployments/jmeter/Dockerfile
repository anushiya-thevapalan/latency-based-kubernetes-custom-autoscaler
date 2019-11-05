#jmeter:v2
#sudo docker build -t anushiya/jmeter:v2 .
#sudo docker push anushiya/jmeter:v2
FROM openjdk:8
 
RUN wget https://www-us.apache.org/dist//jmeter/binaries/apache-jmeter-5.1.1.tgz
RUN tar -xvzf apache-jmeter-5.1.1.tgz
RUN rm apache-jmeter-5.1.1.tgz

# #for installing python
# RUN wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz

RUN mv apache-jmeter-5.1.1 /jmeter
ENV JMETER_HOME /jmeter

# Add Jmeter to the Path
ENV PATH $JMETER_HOME/bin:$PATH

RUN apt-get update; \
    apt-get install python3.5 -y
# RUN set -e; \
#     apt-get update; \
#     apt-get install -y --no-install-recommends \
#         software-properties-common \
#     ; \
#     apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9; \
#     apt-add-repository 'deb http://repos.azulsystems.com/debian stable main'; \
#     apt-get update; \
#     apt-get install -y --no-install-recommends \
#         zulu-8 \
#     ; \
#     apt-get clean; \
#     rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*

# COPY jmeter-demo.sh dest

# ENTRYPOINT 
