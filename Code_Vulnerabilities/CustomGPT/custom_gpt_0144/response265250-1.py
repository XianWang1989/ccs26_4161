import postgresql

def connect_to_db():
    # Force TCP by using 127.0.0.1
    db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')
    print("Connection successful")
    return db

try:
    db = connect_to_db()
except Exception as e:
    print(f"Database connection failed: {e}")
