from flask import Flask

app = Flask(__name__)
@app.route('/')
def msg():
    return '<marquee><h1>Hello World</h1><h2>Hello World</h2><h3>Hello World</h3><h4>Hello World</h4><h5>Hello World</h5><h6>Hello World</h6><h7>Hello World</h7></marquee>'
