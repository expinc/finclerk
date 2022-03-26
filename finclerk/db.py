from peewee import SqliteDatabase

database = None

def init_database(name):
    global database
    database = SqliteDatabase(name)
