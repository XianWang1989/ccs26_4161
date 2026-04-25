
import postgresql

def test_db_connection():
    try:
        # Connect to the PostgreSQL database
        db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')
        # Perform a simple query
        result = db.query('SELECT 1')
        print("Connection successful:", result)
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    test_db_connection()
