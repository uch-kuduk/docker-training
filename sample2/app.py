# app.py - a minimal flask api using flask_restful
from flask import Flask
from db import  connect
import os

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    if 'db_host' not in os.environ:
        db_host = 'localhost'
    else:
        db_host = os.environ['db_host']
    print('db_host= {}'.format(db_host))
    db_connection = connect(db_host)
    app.run(debug=True, use_reloader=False, host='0.0.0.0')

