
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connection established")
    connection.close()
except SQLAlchemyError as e:
    print(f"Error: {e}")
