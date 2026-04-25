
import postgresql

def get_db_connection():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print(f"Error: {e}")
        # Handle the exception or raise it further
    except Exception as e:
        print(f"Another error occurred: {e}")

# Usage
with get_db_connection() as db:
    # Perform database operations
    pass
