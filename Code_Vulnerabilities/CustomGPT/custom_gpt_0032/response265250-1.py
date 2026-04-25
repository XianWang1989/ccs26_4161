
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_session():
    # Adjust your connection string as necessary
    DATABASE_URL = "postgresql://username:password@localhost:5432/db_name"

    # Create an engine instance
    engine = create_engine(DATABASE_URL)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    return session

# Usage
try:
    session = get_db_session()
    # Perform database operations...
except Exception as e:
    print(f"Error: {e}")
