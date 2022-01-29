from flask import Flask

import multilangdia.a

app = Flask(__name__)


@app.route("/")
def hello_world():
    multilangdia.a.plt1()
    return "<p>Created diagram</p>"


