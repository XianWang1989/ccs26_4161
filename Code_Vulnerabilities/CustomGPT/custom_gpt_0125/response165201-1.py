
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
    # Read the entire file
    content = f.read()
    # Split the content at each ';'
    queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Only execute if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")
            db.rollback()  # Rollback in case of error

# Close the cursor and database connection
cursor.close()
db.close()
