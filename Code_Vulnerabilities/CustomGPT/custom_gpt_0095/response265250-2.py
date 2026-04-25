
import postgresql

def connect_db():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        print("Connection successful!")
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print("Connection error:", e)
    except PermissionError as e:
        print("Permission denied:", e)

# Usage
connection = connect_db()
