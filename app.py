from flask import Flask, render_template
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


@app.route('/Ereignis')
def ereignis():
    event = "Hallo Moritz"
    return render_template("Ereignis.html", event = event)


@app.route('/Schaden')
def schaden():
    event = "Hallo Alina"
    return render_template("Schaden.html", event = event)