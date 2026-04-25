
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read entire content
    content = file.read()
    # Split by ';' and remove any extra whitespace
    queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}. Error: {e}")

# Commit changes
db.commit()

# Close cursor and connection
cursor.close()
db.close()
