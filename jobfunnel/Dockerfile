FROM python:alpine

WORKDIR  /usr/src/jobfunnel

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

COPY my_settings.yml ./my_settings.yml

RUN python setup.py install




