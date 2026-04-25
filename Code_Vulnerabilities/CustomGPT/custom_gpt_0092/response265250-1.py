
import postgresql

def test_db_connection():
    try:
        # Replace with your actual username, password, and database name
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        print("Connection successful!")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_db_connection()
