
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

cursor = db.cursor()

# Open the file and read the content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the file content into individual queries
queries = file_content.split(';')

# Execute each query
for query in queries:
    if query.strip():  # Check if the query is not empty
        try:
            cursor.execute(query.strip())
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query.strip()}\nError: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
