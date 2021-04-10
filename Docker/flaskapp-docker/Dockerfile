FROM tensorflow/tensorflow:2.4.1
MAINTAINER mohitkeshwani68@gmail.com

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
COPY flaskapp /opt/

RUN pip3 install -r requirements.txt
WORKDIR /opt/


CMD python3 app.py runserver 0.0.0.0:8000