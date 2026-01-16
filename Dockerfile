FROM python:3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y default-jdk wget unzip && \
    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.zip && \
    unzip allure-commandline-2.27.0.zip -d /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure

COPY . .

CMD ["pytest", "--alluredir", "allure-results"]
