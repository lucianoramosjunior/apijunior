from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    numero = str(random.random())
    return f'Hello World ! {numero}'

if __name__ == '__main__':
    app.run(debug=True)