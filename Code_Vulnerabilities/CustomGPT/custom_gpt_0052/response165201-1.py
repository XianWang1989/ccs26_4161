
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
    content = f.read()

# Split the content by ';' and remove extra whitespace
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        continue  # Skip to next query on error

# Commit the changes
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()
