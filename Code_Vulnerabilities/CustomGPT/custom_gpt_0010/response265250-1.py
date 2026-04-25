
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Database configuration
DB_USER = os.getenv('DB_USER', 'username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'your_password')
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'db_name'

# Create the database engine
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Test the connection
    connection = engine.connect()
    print("Connection successful!")
except Exception as e:
    print(f"Failed to connect to database: {e}")
finally:
    session.close()
