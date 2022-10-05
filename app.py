from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, internet. This is a python web application using GitOps!'
