
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

cursor = db.cursor()

# Read the file and split queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()
    queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}")
            print(f"Error: {e}")
            db.rollback()  # Rollback in case of error

# Close the database connection
cursor.close()
db.close()
