
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

# Create a new database session
engine = create_engine(DATABASE_URL, connect_args={'options': '-csearch_path=your_schema_name'})
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

try:
    # Test the connection
    session.execute('SELECT 1')
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
finally:
    session.close()
