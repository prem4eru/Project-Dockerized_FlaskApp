# dockerapp.py
from flask import Flask

dockerapp = Flask(__name__)

@dockerapp.route('/')
def hello_world():
    return 'Hello, Dockerized Flask App!'

if __name__ == '__main__':
    dockerapp.run(host='0.0.0.0', port=5000)