
import postgresql

def connect_to_db():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except postgresql.exceptions.ConnectionRejectionError as e:
        print("Connection rejected:", e)
    except postgresql.exceptions.ClientCannotConnectError as e:
        print("Could not connect to the server:", e)
    except PermissionError as e:
        print("Permission denied:", e)
    return None

db_connection = connect_to_db()
if db_connection:
    print("Connected to the database!")
