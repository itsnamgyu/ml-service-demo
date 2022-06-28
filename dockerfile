FROM ubuntu:18.04

MAINTAINER DonghoonHan <dhk1349@gmail.com>
LABEL "purpose"="demo"

EXPOSE 8000
RUN apt-get update 
RUN apt-get install git -y 
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

RUN git clone "https://github.com/itsnamgyu/ml-service-demo" 
WORKDIR ./ml-service-demo
RUN pip3 install -r requirements.txt

RUN python3 manage.py migrate
RUN python3 manage.py runserver 0.0.0.0:8000

