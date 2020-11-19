from flask import Flask

app = Flask(__name__)
@app.route('/')
def msg():
    return '<marquee><h1>Hello World</h1><h2>Hello World</h2><h3>Hello World</h3><h4>Hello World</h4><h5>Hello World</h5><h6>Hello World</h6><h7>Hello World</h7></marquee>'

@app.route('/hello')
def msg1():
    return '<h1>Hello!<h1>'

@app.route('/login')
def msg2():
    return '<h1>yes<h1>'

@app.route('/world')
def msg3():
    return '<h1>Hello World!<h1>'

@app.route('/item')
def msg4():
    return '<h1>Hello Item!<h1>'
