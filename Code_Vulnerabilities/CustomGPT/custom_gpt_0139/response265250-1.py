
import os
import postgres

def get_db_connection():
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        raise Exception("Database URL not set in environment variables")

    try:
        db = postgres.open(db_url)
        print("Connection established!")
        return db
    except postgres.ClientCannotConnectError as e:
        print(f"Error: {str(e)}")
        raise

# Usage in your Pyramid app
db_connection = get_db_connection()
