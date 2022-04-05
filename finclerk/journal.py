import re
from . import db
from .model import *
from typing import List

product_types = (
    "STOCK",
    "FUND",
    "FUTURE",
    "OPTION"
)

trade_sides = (
    "BUY",
    "SELL"
)

# YYYY-MM-DD
datetime_pattern = r"\d\d\d\d-\d\d-\d\d"

def add_product(account_id, code, name, type) -> Product:
    # TODO: validate code
    if type not in product_types:
        raise Exception("Invalid product type: {}".format(type))

    with db.database.atomic():
        account = Account.select().where(Account.id == account_id).get()
        return Product.create(account=account, code=code, name=name, type=type)

def _validate_trade(side, price, quantity, date):
    if not re.match(datetime_pattern, date):
        raise Exception("Invalid date format: {}, expects: YYYY-MM-DD".format(date))
    if side not in trade_sides:
        raise Exception("Invalid trade side: {}".format(side))
    if price <= 0:
        raise Exception("Price must be positive")
    if quantity <= 0:
        raise Exception("Quantity must be positive")

def add_trade(product_id, side, price, quantity, date) -> Trade:
    _validate_trade(side, price, quantity, date)
    with db.database.atomic():
        product = Product.select().where(Product.id == product_id).get()
        return Trade.create(product=product, side=side, price=price, quantity=quantity, datetime=date)

def get_trades_of_product(product_id) -> List[Trade]:
    with db.database.atomic():
        return Trade.select().where(Trade.product_id == product_id)

def update_trade(id, side, price, quantity, date) -> int:
    _validate_trade(side, price, quantity, date)
    with db.database.atomic():
        trade = Trade.select().where(Trade.id == id).get()
        trade.side = side
        trade.price = price
        trade.quantity = quantity
        trade.datetime = date
        return trade.save()

def delete_trade(id) -> int:
    with db.database.atomic():
        trade = Trade.select().where(Trade.id == id).get()
        return trade.delete_instance()
