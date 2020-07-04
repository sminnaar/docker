from flask import Flask

app = Flask(__name__)
@app.route('/')
def msg():
    return '<span><h1>Hello World</h1><span>'
