from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Kyra Louise Jordan, welcome to malik office!'
