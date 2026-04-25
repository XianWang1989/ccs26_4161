
from sqlalchemy import create_engine

# Replace 'username', 'password', 'database' with your details
DATABASE_URL = 'postgresql://username:password@localhost:5432/database'

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals():
        connection.close()
