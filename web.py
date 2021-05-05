from flask import Flask

import test

app = Flask(__name__)


@app.route('/')
def home():
    return test.currentValues()


@app.route('/all')
def hello():
    return test.printValues()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
