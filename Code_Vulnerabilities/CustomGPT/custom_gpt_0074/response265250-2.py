
import postgresql

try:
    # Attempt to connect to the PostgreSQL server
    db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')
    print("Connection successful!")
except postgresql.exceptions.ClientCannotConnectError as e:
    print("Could not connect to the database:", e)
except Exception as e:
    print("An error occurred:", e)
