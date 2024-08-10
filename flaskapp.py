from flask import Flask

flaskapp = Flask(__name__)

@flaskapp.route('/')
def hello_world():
    return 'Hello, Simple Flask App!'

if __name__ == '__main__':
    flaskapp.run(debug=True)