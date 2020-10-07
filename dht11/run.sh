#!/bin/bash

export FLASK_APP=./dht11-app.py
export FLASK_DEBUG=0

flask run --host=0.0.0.0 --port=5000

docker-compose up -d
