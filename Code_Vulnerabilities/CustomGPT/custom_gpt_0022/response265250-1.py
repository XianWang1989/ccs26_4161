
import postgresql

# Example connection code
try:
    db = postgresql.open('pq://username:password@localhost:5432/db_name')
    print("Connection successful!")
except postgresql.exceptions.ClientCannotConnectError as e:
    print(f"Connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
