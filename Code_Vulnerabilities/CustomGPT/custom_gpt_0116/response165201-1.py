
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

# Split the content into individual queries using ';' as the delimiter
queries = file_content.split(';')

# Execute each query
for query in queries:
    # Strip whitespace and check if the query is not empty
    query = query.strip()
    if query:
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit changes if necessary
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
