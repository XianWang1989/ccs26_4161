
import postgresql

def get_db_connection():
    try:
        db = postgresql.open('pq://username:password@localhost:5432/db_name')
        return db
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        print("Database connection successful.")
    else:
        print("Database connection failed.")
