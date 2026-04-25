
from postgresql import Helpers, connect

# Replace these values with your actual database details
db_user = 'your_username'
db_password = 'your_password'
db_name = 'your_db_name'
db_host = 'localhost'  # or your server IP
db_port = 5432  # default PostgreSQL port

try:
    # Establishing the connection
    db_url = f'pq://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    db = connect(db_url)

    # You can now execute queries
    result = db.execute('SELECT * FROM your_table;')
    print(Helpers.to_list(result))

except Exception as e:
    print(f"An error occurred: {e}")
