from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
import os
from os import environ

app = Flask(__name__)
# app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

@app.get("/ping")
def application():
    return make_response(jsonify({"status": "live"}), 200)


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_type = db.Column(db.String(80), nullable=False)
    currency_pair =  db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id':self.id, 'order_type': self.order_type, 'price': self.price, 'quantity': self.quantity}

db.create_all()



    
@app.route('/orders', methods=['GET'])
def get_orders():
    try:    
        orders = Order.query.all()
        return make_response(jsonify(order.json() for order in orders), 201)   
    except Exception as e:
        return make_response(jsonify({"message":"Error getting all orders", "Exception": e}), 500)
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port="4000")