
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    content = f.read()

# Split the content into individual queries
queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes to the database
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")
            db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
