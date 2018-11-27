
from flask import (
    Flask, render_template, redirect, request, url_for, session
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/test')
def hello_test():
    return 'Hello, TEST!'

@app.route('/template')
def templates():
    return render_template('sample.html', title='template test')

if __name__ == '__main__':
    app.run()
