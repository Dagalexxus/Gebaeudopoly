from flask import Flask, render_template, session, redirect, request, url_for, request, flash
from flask_session import Session
from tempfile import mkdtemp


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def homepage():
    return render_template("index.html")