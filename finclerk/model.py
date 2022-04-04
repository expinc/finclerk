from . import db
from peewee import *

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = db.database

class Account(BaseModel):
    name = TextField(unique=True)
    password = TextField()

    class Meta:
        table_name = 'accounts'

class Product(BaseModel):
    account = ForeignKeyField(column_name='account_id', field='id', model=Account)
    code = TextField(unique=True)
    name = TextField()
    type = TextField()

    class Meta:
        table_name = 'products'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class Trade(BaseModel):
    datetime = TextField()
    price = FloatField()
    product = ForeignKeyField(column_name='product_id', field='id', model=Product)
    quantity = FloatField()
    side = TextField()

    class Meta:
        table_name = 'trades'
