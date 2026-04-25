
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_session():
    DATABASE_URL = "postgresql://username:password@localhost:5432/db_name"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

def my_view(request):
    try:
        session = get_db_session()
        # Test the query
        result = session.execute('SELECT 1')
        return {'result': result.fetchone()}
    except Exception as e:
        return {'error': str(e)}
