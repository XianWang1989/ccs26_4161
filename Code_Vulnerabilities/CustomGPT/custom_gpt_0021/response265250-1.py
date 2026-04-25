
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

# Database connection string
DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create an engine instance
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

try:
    # Create a session and check the connection
    session = Session()
    connection = session.connection()
    print("Connection successful!")
except Exception as e:
    logging.error(f"Failed to connect to the database: {e}")
finally:
    session.close()
