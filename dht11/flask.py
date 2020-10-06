#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')

def metrics():
    return "Hello World!"
    # umid, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)
    # if umid is not None and temp is not None:
    #     return '# HELP local_temp local temperature\n# TYPE local_temp gauge\nlocal_temp {}\n# HELP local_humidity local humidity\n# TYPE local_humidity gauge\nlocal_humidity {}\n'.format(int(temp), int(umid)), 200, {'Content-Type': 'text/plain; charset=utf-8'}
    # else:
    #     return 'Could not read from DHT11.', 200, {'Content-Type': 'text/plain; charset=utf-8'}
