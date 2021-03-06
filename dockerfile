FROM ubuntu:18.04

MAINTAINER DonghoonHan <dhk1349@gmail.com>
LABEL "purpose"="demo"

EXPOSE 8000
RUN apt-get update 
RUN apt-get install git -y 
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

RUN apt-get install curl -y
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash
RUN apt-get install -y nodejs

ARG CACHEBUST=1
RUN echo "$CACHEBUST"
RUN git clone "https://github.com/itsnamgyu/ml-service-demo" 

WORKDIR ./ml-service-demo/app
RUN npm install
RUN npm run build

WORKDIR ..
RUN pip3 install --no-cache-dir  -r requirements.txt


CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]

