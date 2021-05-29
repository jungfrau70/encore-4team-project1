FROM python:3.8.9
ADD ./python-flask /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt