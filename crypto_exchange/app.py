import os
from os import environ
from flask import Flask, jsonify, request, make_response
from services.order import OrderService
from database.db import db
import json
import logging
import traceback


app = Flask(__name__)
app.debug = True
app.logger.setLevel(logging.DEBUG)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@postgres-service:5432/postgres"
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")

db.init_app(app)

service = OrderService()

@app.get("/ping")
def application():
    return make_response(jsonify({"status": "live"}), 200)


@app.get("/")
def appln():
    return make_response(jsonify({"status": "live"}), 200)

with app.app_context():
    from models.order import Order  # noqa: F401
    db.create_all()

@app.route("/createOrder", methods=["POST"])
def create_order():
    try:
        app.logger.info("createOrder started............")
        data = request.get_json()
        app.logger.info(data)

        service.post(data)

        return make_response(jsonify({"message":"Order created successfully"}), 201)
    except Exception  as e:
        app.logger.error(e)
        traceback.print_exc()
        return make_response(jsonify({"message":"Error in creating order", "Exception": e}), 500)

@app.route("/updateOrder", methods=["PUT"])
def update_order():
    try:
        app.logger.info("updateOrder started............")
        data = request.get_json()
        app.logger.info(data)
       
        order = service.put(data)
        if not order:
            return make_response(jsonify({'error': 'Order not found'}), 404)
        return make_response(jsonify({"order": order.json_()}), 201)
    
    except Exception  as e:
        app.logger.error(e)
        traceback.print_exc()
        return  make_response(jsonify({"message":"Error in updating order", "Exception": e}), 500)
    
@app.route("/getOrders", methods=["GET"])
def get_orders():
    try:
        app.logger.info("getOrder started........")
        orders = service.get_all()
        resp = [order.json_() for order in orders]
        return make_response(jsonify({"orders": resp}), 200)
    except Exception as e:
        app.logger.error(e)
        traceback.print_exc()
        return make_response(jsonify({"message":"Error getting all orders", "Exception": e}), 500)


@app.route("/getOrderById/<id>", methods=["GET"])
def get_order_by_id(id):
    try:
        app.logger.info("getOrderById started........")
        order = service.get(id)
        return make_response(jsonify({"orders": order.json_()}), 200)
    except Exception  as e:
        app.logger.error(e)
        traceback.print_exc()
        return  make_response(jsonify({"message":"Error in finding order", "Exception": e}), 500)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port="5000")