
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/db_name"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Example query
try:
    result = session.execute("SELECT * FROM some_table;")
    for row in result:
        print(row)
except Exception as e:
    print(f"Error: {e}")
finally:
    session.close()
