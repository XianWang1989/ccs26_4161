
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/db_name"

def get_db_session():
    engine = create_engine(DATABASE_URL, connect_args={"timeout": 5})
    Session = sessionmaker(bind=engine)
    return Session()

def example_db_usage():
    session = get_db_session()
    try:
        # Example query
        result = session.execute("SELECT * FROM some_table")
        for row in result:
            print(row)
    finally:
        session.close()
