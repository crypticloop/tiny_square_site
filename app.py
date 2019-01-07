from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is the beginings of the tiny square site"
