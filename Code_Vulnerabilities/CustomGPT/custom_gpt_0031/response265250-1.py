
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

try:
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Test connection
    session.execute('SELECT 1')
    session.close()
except Exception as e:
    print(f"Error: {e}")
