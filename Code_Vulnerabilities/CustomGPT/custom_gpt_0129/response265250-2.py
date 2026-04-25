
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set the connection string (ensure correct credentials)
connection_string = "postgresql://username:password@127.0.0.1:5432/db_name"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

try:
    # Test the connection
    result = session.execute('SELECT 1')
    print("Connection successful:", result.fetchall())
except Exception as e:
    print("Error connecting to the database:", e)
finally:
    session.close()
