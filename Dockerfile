FROM python:3.10-alpine

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . /

RUN pip install --no-cache-dir -r requirements.txt
#RUN #pip install --no-cache-dir --upgrade -r requirements.txt
