
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a scoped session for database interactions
db_session = scoped_session(sessionmaker(bind=engine))

# Example function to test database connection
def test_db_connection():
    try:
        conn = db_session()
        # Execute a simple query
        result = conn.execute("SELECT 1")
        print(result.fetchone())
    except Exception as e:
        print(f"Database connection failed: {e}")
    finally:
        db_session.remove()
