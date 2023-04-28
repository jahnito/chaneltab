from flask_wtf import FlaskForm, CSRFProtect
from wtforms import TextAreaField, StringField, SelectField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from libfunc import get_area_owners, get_areas, get_regions
from config import DB


class AddAddressForm(FlaskForm):
    area_id = SelectField("Район: ", choices=[('', '-- Выберите значение --')] + get_areas(DB, scale=2))
    city = StringField("Населенный пункт: ")
    street = StringField("Улица: ")
    building = StringField("Номер строения/корпус/литер: ")
    region = SelectField("Регион: ", choices=get_regions(DB))
    area_owner = SelectField("Юрисдикция / Принадлежность: ", choices=[('', '-- Выберите значение --')] + get_area_owners(DB))
    submit = SubmitField("Сохранить")


class EditAddressForm(FlaskForm):
    id = HiddenField()
    area_id = SelectField("Район: ", choices=get_areas(DB, scale=2))
    city = StringField("Населенный пункт: ")
    street = StringField("Улица: ")
    building = StringField("Номер строения/корпус/литер: ")
    region = SelectField("Регион: ", choices=get_regions(DB))
    area_owner = SelectField("Юрисдикция / Принадлежность: ", choices=get_area_owners(DB))
    submit = SubmitField("Редактировать")


class AddAreaForm(FlaskForm):
    id = StringField("ID Района: ")
    area_name = StringField("Наименование района: ")
    description = TextAreaField("Дополнительное описание: ")
    submit = SubmitField("Сохранить")


class EditAreaForm(FlaskForm):
    id = StringField("ID района: ")
    area_name = StringField("Наименование района: ")
    description = TextAreaField("Описание: ")
    submit = SubmitField("Редактировать")
