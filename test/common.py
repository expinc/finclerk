from finclerk import db
from finclerk import model
import os

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    data_sql = f.read().decode('utf8')

def init_app():
    db.init_schema()
    db.execute_script(data_sql)
