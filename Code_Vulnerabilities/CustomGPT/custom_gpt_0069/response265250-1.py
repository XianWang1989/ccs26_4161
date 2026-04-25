
import postgresql

# Change 'localhost' to '127.0.0.1' to enforce TCP connection
db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')

# Example query
try:
    with db.transaction():
        results = db.query('SELECT * FROM your_table')
        for row in results:
            print(row)
except postgresql.exceptions.ConnectionError as e:
    print("Error connecting to the database:", e)
