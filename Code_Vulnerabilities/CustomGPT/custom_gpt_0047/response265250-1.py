
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create an engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Use session to interact with the database
try:
    # Example query
    result = session.execute('SELECT 1')
    for row in result:
        print(row)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()
