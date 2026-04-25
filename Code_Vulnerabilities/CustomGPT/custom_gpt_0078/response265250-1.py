
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def connect_to_database():
    try:
        # Use TCP instead of Unix socket
        engine = create_engine('postgresql+psycopg2://username:password@127.0.0.1:5432/db_name')
        connection = engine.connect()
        print("Connection successful!")
        return connection
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    connect_to_database()
