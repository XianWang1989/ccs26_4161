
import postgresql

try:
    # Replace with your actual credentials
    db = postgresql.open("pq://username:password@localhost:5432/db_name")

    # Perform a sample query
    result = db.query("SELECT * FROM your_table LIMIT 5;")

    for row in result:
        print(row)

except postgresql.exceptions.ClientCannotConnectError as e:
    print("Connection failed:", e)

except Exception as e:
    print("An error occurred:", e)
