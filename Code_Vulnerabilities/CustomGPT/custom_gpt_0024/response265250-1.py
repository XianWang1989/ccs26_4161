
import postgresql

def test_db_connection():
    try:
        # Change these values to your configuration
        db_url = "pq://username:password@localhost:5432/db_name"
        db = postgresql.open(db_url)

        # Execute a simple query
        result = db.query("SELECT 1")
        print("Query result:", result)

    except postgresql.exceptions.ClientCannotConnectError as e:
        print("Connection failed:", e)
    except Exception as e:
        print("An error occurred:", e)

# Call the function to test the connection
test_db_connection()
