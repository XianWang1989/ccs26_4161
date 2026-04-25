
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

def get_db_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage in a view
def my_view(request):
    session = get_db_session()
    try:
        # Your database operations here
        pass
    finally:
        session.close()
