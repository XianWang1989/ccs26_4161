
from postgresql import connect
from postgresql.exceptions import ClientCannotConnectError

try:
    db_uri = "pq://username:password@localhost:5432/db_name"
    db = connect(db_uri)
except ClientCannotConnectError as e:
    print(f"Error connecting to database: {e}")
