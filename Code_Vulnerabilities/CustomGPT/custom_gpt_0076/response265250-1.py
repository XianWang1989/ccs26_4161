
import postgresql

try:
    db = postgresql.open('pq://username:password@localhost:5432/db_name')
    print("Connected to the database!")
except postgresql.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
