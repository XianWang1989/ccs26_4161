
import postgresql

db = postgresql.open('pq://username:password@localhost/db_name')
print(db.query("SELECT 1;"))
