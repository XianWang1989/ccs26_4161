
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection string
DB_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create engine
engine = create_engine(DB_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example function to test database connection
def test_connection():
    try:
        # Test the connection
        session.execute("SELECT 1")
        print("Database connection successful!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

# Call the test function
test_connection()
