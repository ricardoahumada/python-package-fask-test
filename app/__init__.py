from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask import jsonify, request
from collections import namedtuple
import json

from app.customer.customer_manager import CustomerManager
from app.customer.customer import Customer

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
toolbar = DebugToolbarExtension(app)

customerManager = CustomerManager()
customerManager.customers = []


@app.route('/api/v1/customers/', methods=['GET'])
def get_customers():
    return json.dumps(customerManager.get_customers(),default=vars)


@app.route('/api/v1/customers/', methods=['POST'])
def add_customers():
    customer = Customer(**request.json)
    customer = customerManager.add_customer(customer)
    return customer.toJSON()
