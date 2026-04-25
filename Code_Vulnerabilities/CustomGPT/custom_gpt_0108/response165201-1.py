
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    queries = f.read().split(';')  # Split the contents by ';'

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as err:
            print(f"Error executing query: {err}")
            db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
