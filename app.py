import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return '<h1>Hello, Docker!</h1><img src="https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png">'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
