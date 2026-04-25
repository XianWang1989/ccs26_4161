
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt') as f:
    # Read the entire file contents
    file_contents = f.read()

# Split the contents by the semicolon delimiter
queries = file_contents.split(';')

# Iterating over each query and executing it
for query in queries:
    # Strip whitespace and check if the query is not empty
    query = query.strip()
    if query:
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except Exception as e:
            print(f"Error executing query: {query}\n{e}")

# Close the cursor and the database connection
cursor.close()
db.close()
