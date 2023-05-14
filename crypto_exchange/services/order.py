from models.order import Order
import logging
import json
from flask import jsonify, make_response
import traceback
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class OrderService():

    def __init__(self) -> None:
        pass


    def get(self, id):
        order = Order.get_by_id(id)
        return order
    
        
    def post(self, data):
        new_order = Order(order_type=data['order_type'], currency_pair = data['currency_pair'], price=data['price'], quantity=data['quantity'])
        new_order.add()
        
    
    def put(self, data):
        update_order = Order(order_type=data['order_type'], currency_pair = data['currency_pair'], price=data['price'], quantity=data['quantity'])
        update_order.id = data["id"]
        return update_order.update()

       
        
    def get_all(self):
        return Order.get_all()
            
        



    