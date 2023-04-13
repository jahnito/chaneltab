#coding:utf8


import sqlite3
import os
from sys import platform
from flask import Flask, render_template

app = Flask(__name__)
# Тут мелкая боль разработки под виндой, хех, путь коварен.
if platform == 'win32':
    DB = os.getcwd()+'\\db\\nettab.db'
else:
    DB = 'db/nettab.db'

def get_addresses(db: str) -> list:
    '''
    Все адреса
    '''
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("""SELECT address.root_to, address.city, address.street, address.building, type_channel.name, type_phys_channel.name
from
main, address, type_channel, type_phys_channel
where
main.address_id = address.id
AND
main.type_channel_id = type_channel.id
AND
main.type_phys_channel_id = type_phys_channel.id""")
    return [i for i in cursor]


@app.route('/')
def index():
    addresses = get_addresses(DB)
    return render_template('index.html', addresses=addresses)


app.run(host='127.0.0.1', port=8080)