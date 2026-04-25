
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()

# Split the content by semicolon to separate each query
queries = file_content.split(';')

# Execute each query
for query in queries:
    # Strip whitespace and ignore empty queries
    query = query.strip()
    if query:
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\nError: {e}")
            db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
