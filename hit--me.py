from time import sleep

from flask import Flask

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
