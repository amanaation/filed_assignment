from flask import Flask, request
from flask import Flask, render_template, request
from main_functions import *
import ast

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route("/post", methods=['GET'])
def process():
    sent_data = {}
    for key, value in request.args.items():
        sent_data[key] = str(value)
    message = process_transaction(sent_data)
    if message is True:
        message = "Payment is processed: 200 OK"
    return "<h1> <center> " + message + "</center></h1>"

if __name__ == "__main__":
    app.run(debug=True)
