import os
import sqlite3
from peewee import SqliteDatabase

with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'rb') as f:
    schema_sql = f.read().decode('utf8')

dbname = os.environ["DATABASE_NAME"]
database = SqliteDatabase(dbname)

def execute_script(script):
    # Here may execute a multi-query script.
    # Therefore connect database by sqlite3 API directly.
    try:
        connection = sqlite3.connect(dbname)
        connection.executescript(script)
    finally:
        if connection:
            connection.close()

def init_schema():
    execute_script(schema_sql)
