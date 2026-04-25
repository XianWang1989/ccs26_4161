
import postgresql

# Replace with your actual credentials
db = postgresql.open('pq://username:password@localhost:5432/db_name')

# Example query
try:
    with db.xact():
        result = db.prepare("SELECT * FROM your_table")()
        for row in result:
            print(row)
except postgresql.exceptions.ClientCannotConnectError as e:
    print(f"Connection failed: {e}")
