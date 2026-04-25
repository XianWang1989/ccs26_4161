
from sqlalchemy import create_engine

# Replace 'username', 'password', 'db_name' with your credentials
DATABASE_URL = 'postgresql://username:password@127.0.0.1:5432/db_name'

engine = create_engine(DATABASE_URL)

def connect_database():
    try:
        connection = engine.connect()
        print("Connection successful!")
        return connection
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call connect_database() within your WSGI application
