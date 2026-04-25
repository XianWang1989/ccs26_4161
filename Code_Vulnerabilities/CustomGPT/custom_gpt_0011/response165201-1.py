
import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the content by `;` to get individual queries
queries = file_content.split(';')

# Execute each query
for query in queries:
    if query.strip():  # Check if the query is not empty
        try:
            cursor.execute(query.strip())  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query.strip()} - {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
