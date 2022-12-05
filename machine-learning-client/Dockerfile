FROM python:3-slim

WORKDIR /ml-app

ADD . /ml-app

RUN pip3 install --trusted-host pypi.python.org -r web-app/docker-requirements.txt

CMD ["python3", "./web-app/app.py"]