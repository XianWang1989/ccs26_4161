
import postgresql

def get_db_connection():
    try:
        # Adjusted connection string as needed
        db = postgresql.open("pq://username:password@127.0.0.1:5432/db_name")
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Could not connect to database: {e}")
        return None
