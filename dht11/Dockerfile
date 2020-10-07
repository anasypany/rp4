FROM python:buster

COPY . /dht11

RUN apt-get update && \
    apt-get upgrade -y && \
    pip3 install -r /dht11/requirements.txt && \
    apt-get install libgpiod2 && \
    apt-get clean

WORKDIR /dht11

CMD ["python3", "dht11-app.py"]
