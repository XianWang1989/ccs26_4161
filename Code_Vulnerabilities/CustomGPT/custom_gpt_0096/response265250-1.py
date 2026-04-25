
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Update with your actual database credentials
DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example query
try:
    result = session.execute("SELECT * FROM some_table")
    for row in result:
        print(row)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()
