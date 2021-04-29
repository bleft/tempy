from flask import Flask

import test

app = Flask(__name__)

@app.route('/')
def hello():
    return test.printValues()
