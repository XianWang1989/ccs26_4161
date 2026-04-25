
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection string
DB_USER = 'username'
DB_PASS = 'password'
DB_NAME = 'db_name'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Create a database engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

try:
    # Create a session
    session = Session()

    # Example query
    result = session.execute("SELECT 1").fetchone()
    print(result)

except Exception as e:
    print(f"Error occurred: {e}")
finally:
    session.close()
