FROM python:3.10-alpine

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . /

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ./Tests/ui_tests
RUN ls
RUN pytest --browser=local_chrome -s -v
