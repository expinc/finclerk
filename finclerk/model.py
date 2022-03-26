import db
from peewee import *

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = db.database

class Accounts(BaseModel):
    account_name = TextField(unique=True)
    password = TextField()

    class Meta:
        table_name = 'accounts'

class Products(BaseModel):
    account = ForeignKeyField(column_name='account_id', field='id', model=Accounts)
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

class Trades(BaseModel):
    datetime = TextField()
    price = FloatField()
    product = ForeignKeyField(column_name='product_id', field='id', model=Products)
    quantity = FloatField()
    side = TextField()

    class Meta:
        table_name = 'trades'

