from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired
from libfunc import get_areas, get_regions
from config import DB


class AddAddressForm(FlaskForm):
    area = StringField("Район: ")
    city = StringField("Населенный пункт: ")
    street = StringField("Улица: ")
    building = StringField("Номер строения/корпус/литер: ")
    region = SelectField("Регион: ", choices=get_regions(DB))
    area_id = SelectField("Юрисдикция / Принадлежность: ", choices=get_areas(DB))
    submit = SubmitField("Загрузить")
