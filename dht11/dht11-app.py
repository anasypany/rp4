#!/usr/bin/python3

from flask import Flask
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)


app = Flask(__name__)


@app.route('/metrics')
def metrics():

    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        return '# HELP temp_celcius local temperature in Celcius\n# TYPE temp_celcius gauge\ntemp_celcius {}\n# HELP temp_fahrenheit local temperature in Fahrenheit\n# TYPE temp_fahrenheit gauge\ntemp_fahrenheit {}\n# HELP humidity_percentage local humidity as a percentage\n# TYPE humidity_percentage gauge\nhumidity_percentage {}\n'.format(int(temperature_c), int(temperature_f), int(humidity)), 200, {'Content-Type': 'text/plain; charset=utf-8'}


    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        return 'Could not read from DHT11.', 200, {'Content-Type': 'text/plain; charset=utf-8'}
    except Exception as error:
        dhtDevice.exit()
        return 'oof.', 404, {'Content-Type': 'text/plain; charset=utf-8'}
        raise error

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
