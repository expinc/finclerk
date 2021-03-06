from . import common
from . import db
from . import marketdata
from .model import *
from typing import List

product_types = (
    "STOCK",
    "FUND",
    # "FUTURE",
    # "OPTION"
)

trade_sides = (
    "BUY",
    "SELL"
)

# YYYY-MM-DD
datetime_pattern = r"\d\d\d\d-\d\d-\d\d"

def add_product(account_id, code, name, type) -> Product:
    if type not in product_types:
        raise Exception("Invalid product type: {}".format(type))

    if_exists = False
    if "STOCK" == type:
        if_exists = marketdata.check_stock_exists(code)
    elif "FUND" == type:
        if_exists = marketdata.check_fund_exists(code)
    if not if_exists:
        raise Exception("Product does not exist: {}".format(code))

    with db.database.atomic():
        if 0 < Product.select().where(Product.account.id == account_id and Product.code == code).count():
            raise Exception("Product code already exists: {}".format(code))

        account = Account.select().where(Account.id == account_id).get()
        return Product.create(account=account, code=code, name=name, type=type)

def get_product(product_id) -> Product:
    with db.database.atomic():
        return Product.select().where(Product.id == product_id).get()

def get_products_in_account(account_id) -> List[Product]:
    with db.database.atomic():
        return Product.select().where(Product.account_id == account_id)

def _validate_trade(side, price, quantity, date):
    common.check_date_format(date)
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
        return Trade.select().where(Trade.product_id == product_id).order_by(Trade.datetime)

def get_trade(id) -> Trade:
    with db.database.atomic():
        return Trade.select().where(Trade.id == id).get()

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
