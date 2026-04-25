
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

try:
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Test connection
    session.execute("SELECT 1")
    logging.info("Database connection established successfully.")
except Exception as e:
    logging.error(f"Database connection error: {e}")
