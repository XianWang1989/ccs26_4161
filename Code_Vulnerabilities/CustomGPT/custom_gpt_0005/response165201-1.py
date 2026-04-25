
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    contents = f.read()

# Split the contents by ';'
queries = contents.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any extra whitespace
    if query:  # Ensure it’s not an empty query
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit changes and close the connection
db.commit()
cursor.close()
db.close()
