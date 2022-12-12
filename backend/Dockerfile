FROM python:3.11
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

FROM ubuntu:trusty
RUN sudo apt-get -y update
RUN sudo apt-get -y upgrade
RUN sudo apt-get install -y sqlite3 libsqlite3-dev

