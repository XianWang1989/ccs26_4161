
import postgresql

try:
    db = postgresql.open("pq://username:password@localhost:5432/db_name")
    print("Connection established!")
except Exception as e:
    print("Error:", e)
