
from postgresql import connect

db_url = "pq://username:password@127.0.0.1:5432/db_name"
connection = connect(db_url)
