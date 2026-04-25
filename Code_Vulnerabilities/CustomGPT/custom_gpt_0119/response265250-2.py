
import postgresql

try:
    # Connect to the PostgreSQL database
    db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')
    # Create a simple query
    result = db.execute('SELECT * FROM your_table LIMIT 5;')

    for row in result:
        print(row)

except postgresql.exceptions.ClientCannotConnectError as e:
    print("Connection failed:", e)

except Exception as e:
    print("An error occurred:", e)
