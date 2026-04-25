
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Split the content into individual queries
queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit each query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
