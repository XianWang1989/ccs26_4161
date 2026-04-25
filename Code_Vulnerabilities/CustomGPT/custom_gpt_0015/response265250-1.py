
import postgresql

# Connection parameters
db = postgresql.open('pq://username:password@localhost:5432/db_name')

# Execute a simple query
try:
    with db.xact():
        result = db.prepare("SELECT 1")()
        print(result)
except postgresql.exceptions.ClientCannotConnectError as e:
    print(f"Connection Error: {e}")
