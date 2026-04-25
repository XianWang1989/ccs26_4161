
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()

# Split the content at each semicolon
queries = content.split(';')

# Execute each query
for query in queries:
    # Strip whitespace and ensure the query is not empty
    query = query.strip()
    if query:  # Only execute non-empty queries
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
