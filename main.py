# coding:utf8
from flask import Flask, request, render_template
from libfunc import *
from libforms import AddAddressForm, AddAreaForm, EditAddressForm, EditAreaForm
from config import DB

app = Flask(__name__)
app.config['SECRET_KEY'] = '0b194d12d2d207912b454db5e529522763433da5676512ba5e3400f37c7b9585'


@app.route('/')
def index():
    tech_pos = tech_possible(DB)
    addresses = get_addresses(DB)
    return render_template('index.html', addresses=addresses, tech_pos=tech_pos)


@app.route('/add_object.html', methods=['GET','POST'])
def add_object():
    if request.method == 'POST':
        addr_data = {}
        addr_data['area_id'] = request.values.get('area_id')
        addr_data['city'] = request.values.get('city')
        addr_data['street'] = request.values.get('street')
        addr_data['building'] = request.values.get('building')
        addr_data['region'] = request.values.get('region')
        addr_data['area_owner'] = request.values.get('area_owner')
        message = add_new_address(DB, addr_data)
        form = AddAddressForm()
        return render_template('add_object.html', addr_data=addr_data, form=form, message=message)
    else:
        form = AddAddressForm()
        return render_template('add_object.html', form=form)


@app.route('/add_area.html', methods=['GET','POST'])
def add_area():
    if request.method == 'POST':
        area_data = {}
        area_data['id'] = request.values.get('id')
        area_data['area_name'] = request.values.get('area_name')
        area_data['description'] = request.values.get('description')
        message = add_new_area(DB, area_data)
        form = AddAreaForm()
        return render_template('add_area.html', area_data=area_data, form=form, message=message)
    else:
        form = AddAreaForm()
        return render_template('add_area.html', form=form)


@app.route('/edit_object.html', methods=['GET','POST'])
def edit_object():
    addresses = get_addresses(DB)
    addr_data = {}
    if request.method == 'POST':
        addr_data['id'] = request.values.get('id')
        addr_data['region'] = request.values.get('region')
        addr_data['area_id'] = request.values.get('area_id')
        addr_data['city'] = request.values.get('city')
        addr_data['street'] = request.values.get('street')
        addr_data['building'] = request.values.get('building')
        addr_data['area_owner'] = request.values.get('area_owner')
    if request.method == 'POST' and request.values.get('step') == '1':
        form = EditAddressForm()
        return render_template('edit_object.html', form=form, step=1)
    elif request.method == 'POST' and request.values.get('step') == '2':
        message = edit_address(DB, addr_data)
        form = EditAddressForm(request.form)
        return render_template('edit_object.html', form=form, step=2, message=message, addr_data=addr_data)
    else:
        return render_template('edit_object.html', addresses=addresses)


@app.route('/edit_area.html', methods=['GET','POST'])
def edit_area():
    areas = get_areas(DB)
    area_data = {}
    if request.method == 'POST':
        area_data['id'] = request.values.get('id')
        area_data['area_name'] = request.values.get('area_name')
        area_data['description'] = request.values.get('description')
    if request.method == 'POST' and request.values.get('step') == '1':
        form = EditAreaForm()
        return render_template('edit_area.html', form=form, step=1)
    elif request.method == 'POST' and request.values.get('step') == '2':
        # message = edit_address(DB, addr_data)
        form = EditAreaForm()
        return render_template('edit_area.html', form=form, step=2) #message=message, addr_data=addr_data)
    else:
        print(areas)
        return render_template('edit_area.html', areas=areas)

app.run(host='127.0.0.1', port=8080)
