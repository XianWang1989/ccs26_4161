
from postgresql import connect

def database_connection():
    try:
        # Update with your actual credentials
        db_url = 'pq://username:password@localhost:5432/db_name'
        db = connect(db_url)
        return db
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    db = database_connection()
    if db:
        print("Connected successfully!")
