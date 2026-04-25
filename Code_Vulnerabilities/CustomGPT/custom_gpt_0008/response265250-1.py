
import postgresql

try:
    # Update these with your actual values
    db = postgresql.open('pq://username:password@localhost:5432/db_name')
    print("Connection established!")
except postgresql.exceptions.ClientCannotConnectError as e:
    print("ClientCannotConnectError:", e)
except Exception as e:
    print("An error occurred:", e)
