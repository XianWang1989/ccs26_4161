
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your actual database credentials
DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create an engine instance
engine = create_engine(DATABASE_URL, connect_args={'sslmode': 'require'})

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Example query
try:
    result = session.execute("SELECT * FROM your_table")
    for row in result:
        print(row)
except Exception as e:
    print(f"Error: {e}")
finally:
    session.close()
