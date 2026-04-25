
from postgresql import asynch

def connect_to_db():
    try:
        db = asynch.Database('pq://username:password@localhost:5432/db_name')
        connection = db.connect()
        print("Connection successful!")
    except Exception as e:
        print("Connection failed:", str(e))

connect_to_db()
