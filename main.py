# coding:utf8
import sqlite3
import os
from sys import platform
from flask import Flask, render_template
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '0b194d12d2d207912b454db5e529522763433da5676512ba5e3400f37c7b9585'

# Тут мелкая боль разработки под виндой, хех, путь коварен.
# Переходи на светлую сторону, ставь Linux!
if platform == 'win32':
    DB = os.getcwd()+'\\db\\nettab.db'
else:
    DB = 'db/nettab.db'


class AddAddressForm(FlaskForm):
    area = StringField("Район: ")
    city = StringField("Населенный пункт: ")
    street = StringField("Улица: ")
    building = StringField("Номер строения/корпус/литер: ")
    region = SelectField("Регион: ", choices=[('1', 'Пермский край'), ('2', 'Тюменская область')])
    area_id = SelectField("Юрисдикция / Принадлежность: ", choices=[('8', 'Свердловский район'), ('17', 'Александровский район')])
    submit = SubmitField("Загрузить")


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


@app.route('/add_object.html')
def add_object():
    form = AddAddressForm()

    return render_template('add_object.html', form=form)


app.run(host='127.0.0.1', port=8080)