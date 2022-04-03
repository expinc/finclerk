from . import db
from .model import *
from typing import List

def add_product(account_id, code, name, type) -> Product:
    # TODO: validate code
    with db.database.atomic():
        account = Account.select().where(Account.id == account_id).get()
        return Product.create(account=account, code=code, name=name, type=type)

def add_trade(product_id, side, price, quantity) -> Trade:
    with db.database.atomic():
        product = Product.select().where(Product.id == product_id).get()
        return Trade.create(product=product, side=side, price=price, quantity=quantity)

def get_trades_of_product(product_id) -> List[Trade]:
    with db.database.atomic():
        return Trade.select().where(Trade.product.id == product_id)

def update_trade(id, side, price, quantity) -> int:
    with db.database.atomic():
        trade = Trade.select().where(Trade.id == id).get()
        trade.side = side
        trade.price = price
        trade.quantity = quantity
        return trade.save()

def delete_trade(id) -> int:
    with db.database.atomic():
        trade = Trade.select().where(Trade.id == id).get()
        return trade.delete_instance()
