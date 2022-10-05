from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Thi is a GitOps pipeline with Jenkins and Amazon EKS cluster!'
