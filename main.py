from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DB = 'db/nettab.db'


def get_addresses(db: str) -> list:
    '''
    Все адреса
    '''
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM address')
    return [i for i in cursor]


@app.route('/')
def index():
    addresses = get_addresses(DB)
    return render_template('index.html', addresses=addresses)
