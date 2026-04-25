
import postgresql

# Change the connection string to use TCP/IP instead of a socket
db = postgresql.open('pq://username:password@127.0.0.1:5432/db_name')
