#coding:utf8


import sqlite3
import os
from sys import platform
from flask import Flask, render_template

app = Flask(__name__)

# Тут мелкая боль разработки под виндой, хех, путь коварен.
# Переходи на светлую сторону, ставь Linux!
if platform == 'win32':
    DB = os.getcwd()+'\\db\\nettab.db'
else:
    DB = 'db/nettab.db'


def tech_possible(db: str) -> dict:
    '''
    Функция возвращает словарь где ключ объект/адрес(id) хранятся кортежи (услуга, тип подключения)
    '''
    result = {}
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("""SELECT technical_possibility.object_id, technical_possibility.service, type_phys_channel.name
                    FROM
                    technical_possibility, type_phys_channel
                    WHERE
                    type_phys_channel.id = technical_possibility.type_phys_channel""")
    for id, service, type in cursor:
        if result.get(id):
            result[id].append((service, type))
        else:
            result[id] = [(service, type)]
    return result


def get_addresses(db: str) -> list:
    '''
    Вывод всех адресов на главной странице
    '''
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("""SELECT region.name, address.area, address.city, address.street, address.building, areas.area_name, address.id
                    FROM
                    address, areas, region
					WHERE
					address.area_id = areas.id
					AND
					region.id = address.region_id""")
    return [ i for i in cursor ]


@app.route('/')
def index():
    tech_pos = tech_possible(DB)
    addresses = get_addresses(DB)
    return render_template('index.html', addresses=addresses, tech_pos=tech_pos)


app.run(host='127.0.0.1', port=8080)