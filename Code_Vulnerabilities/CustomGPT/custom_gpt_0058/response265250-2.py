
import postgresql

try:
    # Example of using TCP/IP connection
    db = postgresql.open("pq://username:password@127.0.0.1:5432/db_name")
    # Do something with the database
    connection = db.query("SELECT * FROM your_table")
    for row in connection:
        print(row)
except postgresql.exceptions.ClientCannotConnectError as e:
    print(f"Unable to connect to the database: {e}")
