from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route('/')
def home():
    return 'hey there!'

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("127.0.0.1")