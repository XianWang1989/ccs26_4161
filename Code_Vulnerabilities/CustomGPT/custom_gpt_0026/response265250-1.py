
from postgresql import connect

def connect_to_db():
    try:
        db_url = 'pq://username:password@localhost:5432/db_name'
        db = connect(db_url)
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")

# Usage
db_connection = connect_to_db()
if db_connection:
    print("Connection established.")
else:
    print("Connection failed.")
