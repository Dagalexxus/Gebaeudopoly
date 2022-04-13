from random import randrange
from flask import Flask, render_template
from flask_session import Session
from tempfile import mkdtemp
import sqlite3


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
    db = sqlite3.connect('spiel.db')
    db_cursor = db.cursor()

    #find random number for event
    event_number = randrange(1,51)

    db_cursor.execute('SELECT Ereignis from Ereignisse WHERE ID = ?', (int(event_number),))
    event = db_cursor.fetchone()
    event = event[0]
    db.close()
    return render_template("ereignis.html", event = event)


@app.route('/Schaden')
def schaden():
    db = sqlite3.connect('spiel.db')
    db_cursor = db.cursor()

    #find random number for event
    event_number = randrange(1,21)

    db_cursor.execute('SELECT Ereignis from Schaden WHERE ID = ?', (event_number,))
    event = db_cursor.fetchone()
    event= event[0]
    db.close()
    return render_template("schaden.html", event = event)