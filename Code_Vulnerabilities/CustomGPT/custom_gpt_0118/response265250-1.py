
import postgresql

db = postgresql.open('pq://username:password@localhost/db_name?host=/var/run/postgresql')
