
import postgresql

def connect_to_db():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        print("Connection successful!")
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print("Could not connect to the database:", e)

# Call the function
connect_to_db()
