# coding:utf8
from flask import Flask, request, render_template
from libfunc import *
from libforms import AddAddressForm, AddAreaForm
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
        addr_data = {}
        # addr_data['area_id'] = request.values.get('area_id')
        # addr_data['city'] = request.values.get('city')
        # addr_data['street'] = request.values.get('street')
        # addr_data['building'] = request.values.get('building')
        # addr_data['region'] = request.values.get('region')
        # addr_data['area_owner'] = request.values.get('area_owner')
        # message = add_new_address(DB, addr_data)
        # form = AddAddressForm()
        # return render_template('add_object.html', addr_data=addr_data, form=form, message=message)
        return render_template('add_area.html', form=form)
    else:
        form = AddAreaForm()
        return render_template('add_area.html', form=form)


app.run(host='127.0.0.1', port=8080)
