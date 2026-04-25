
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_session():
    # Modify connection string as needed
    connection_string = "postgresql://username:password@127.0.0.1:5432/db_name"
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage
session = get_db_session()
# Perform your database operations
