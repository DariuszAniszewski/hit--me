from time import sleep

from flask import Flask
from flask.ext.cache import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route('/')
def hello_world():
    return 'Hit Me application for load testing demonstrations'


@app.route('/mu-012768e9-7817db3b-7bc502ac-f9ff267a')
def blitz_io():
    return "42"


@app.route('/<int:millis>ms')
def delay_for_amount_of_millis(millis):
    sleep(millis / 1000)
    return "This request took like {}ms".format(millis)


@app.route('/increment')
def incremental_delay():
    cache_key = "milliseconds_to_sleep"
    milliseconds_to_sleep = cache.get(cache_key)
    if not milliseconds_to_sleep:
        milliseconds_to_sleep = 0
    sleep(1.0 * milliseconds_to_sleep / 1000)
    cache.set(cache_key, milliseconds_to_sleep + 10, timeout=60)
    return "This request took like {}ms. Next one will be longer".format(milliseconds_to_sleep)


if __name__ == '__main__':
    app.run()
