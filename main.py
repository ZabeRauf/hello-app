from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulation, we started a web app"