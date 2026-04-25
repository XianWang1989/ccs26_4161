
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Update the connection URL to use TCP
DATABASE_URL = "postgresql://username:password@127.0.0.1:5432/db_name"

# Create an engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
