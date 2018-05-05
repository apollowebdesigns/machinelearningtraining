from flask import Flask
app = Flask(__name__)
from time import time

@app.route('/')
def hello_world():
    print('what is now?')
    print(time.now())
    return 'Hello World'

if __name__ == '__main__':
   app.run()