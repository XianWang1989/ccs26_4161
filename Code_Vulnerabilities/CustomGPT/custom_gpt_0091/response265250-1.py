
import postgresql

db = postgresql.open('pq://username:password@/db_name?host=/var/run/postgresql')
