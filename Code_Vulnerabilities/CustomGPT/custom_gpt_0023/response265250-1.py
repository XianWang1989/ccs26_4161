
import os
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/db_name')

def get_db_engine():
    return create_engine(DATABASE_URL)

def get_db_session():
    engine = get_db_engine()
    Session = sessionmaker(bind=engine)
    return Session()

# In your Pyramid view
def my_view(request):
    session = get_db_session()
    # Perform database operations
    ...
