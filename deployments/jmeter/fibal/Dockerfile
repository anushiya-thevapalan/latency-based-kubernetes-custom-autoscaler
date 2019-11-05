FROM java:8
 
RUN wget https://www-us.apache.org/dist//jmeter/binaries/apache-jmeter-5.1.1.tgz
RUN tar -xvzf apache-jmeter-5.1.1.tgz
RUN rm apache-jmeter-5.1.1.tgz

RUN mv apache-jmeter-5.1.1 /jmeter

ENV JMETER_HOME /jmeter

# Add Jmeter to the Path
ENV PATH $JMETER_HOME/bin:$PATH

FROM python:3.6

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=DontWarn

RUN set -e; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        software-properties-common \
    ; \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xB1998361219BD9C9; \
    apt-add-repository 'deb http://repos.azulsystems.com/debian stable main'; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        zulu-8 \
    ; \
    apt-get clean; \
    rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*