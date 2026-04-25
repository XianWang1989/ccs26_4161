
import postgresql

try:
    # Adjust the connection string as needed
    db = postgresql.open('pq://username:password@localhost:5432/db_name')
    print("Connected to the database successfully!")
except postgresql.exceptions.ClientCannotConnectError as e:
    print(f"Connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
