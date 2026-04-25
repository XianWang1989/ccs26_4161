
import postgresql

def connect_to_db():
    try:
        # Update with your actual database information
        db = postgresql.open('pq://username:password@localhost/db_name')
        # Test the connection
        db.prepare("SELECT 1").all()
        print("Connection successful!")
    except postgresql.exceptions.ClientCannotConnectError as e:
        print("Connection failed:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    connect_to_db()
