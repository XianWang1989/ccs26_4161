
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace these with your actual database credentials
DB_USER = 'username'
DB_PASSWORD = 'your_password'
DB_HOST = '127.0.0.1'  # Use TCP/IP instead of Unix socket
DB_PORT = '5432'
DB_NAME = 'db_name'

# Create a SQLAlchemy engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# Example query
try:
    result = session.execute("SELECT * FROM your_table LIMIT 10;")
    for row in result:
        print(row)
except Exception as e:
    print(f"Error: {e}")
finally:
    session.close()
