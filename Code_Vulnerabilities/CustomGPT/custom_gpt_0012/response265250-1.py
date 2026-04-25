
import postgresql

def connect_to_db():
    try:
        # Use proper credentials and database name
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        print("Connection successful!")
        return db
    except postgresql.exceptions.ClientCannotConnectError as e:
        print("Connection failed: ", e)
    except Exception as e:
        print("An error occurred: ", e)

# Call the function to test the connection
connect_to_db()
