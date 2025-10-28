# application.py
from flask import Flask
application = Flask(__name__) # 'application'という名前のオブジェクトが必要

@application.route('/')
def hello():
    return "Hello, Elastic Beanstalk!"

if __name__ == "__main__":
    application.run()