from email import message
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask import jsonify, request
from collections import namedtuple
import json
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

from app.customer.customer_manager import CustomerManager
from app.customer.customer import Customer

app = Flask(__name__)
# app.debug = False
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
toolbar = DebugToolbarExtension(app)
jwt = JWTManager(app)

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

@app.route("/api/v1/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user_id=0
    if email=='user@test.com' and password=='passwordjd':
        user_id=1

    if user_id==0:
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user_id)
    return jsonify({ "token": access_token, "user_id": user_id })

@app.route('/api/v1/restricted', methods=['GET'])
@jwt_required()
def api_get_users():    
    return jsonify({'message':'you are in the restricted area'})
