from flask import Flask

import test

app = Flask(__name__)

@app.route('/')
def home():
    return test.currentValues()

@app.route('/all')
def hello():
    return test.printValues()

