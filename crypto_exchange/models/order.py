from database.db import db
import logging
import traceback
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_type = db.Column(db.String(80), nullable=False)
    currency_pair = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)

    def __init__(self, order_type, currency_pair, price, quantity):
        self.order_type = order_type
        self.currency_pair = currency_pair 
        self.price = price 
        self.quantity = quantity

    def json_(self):
        return {
                'id': self.id, 
                'order_type': self.order_type, 
                'currency_pair': self.currency_pair,
                'price': self.price, 
                'quantity': self.quantity
        }


    @classmethod
    def get_by_id(cls, id):
        return Order.query.get(id)
    
    @classmethod
    def get_all(cls):
        return Order.query.all()
    

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        existing_order = Order.query.get(self.id)
        if not existing_order:
            return None
        existing_order.order_type = self.order_type
        existing_order.currency_pair = self.currency_pair
        existing_order.price = self.price
        existing_order.quantity = self.quantity
        db.session.commit()        

        return Order.get_by_id(self.id)
