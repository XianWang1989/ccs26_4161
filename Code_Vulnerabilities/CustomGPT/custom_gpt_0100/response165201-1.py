
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the text file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_content = f.read()

# Split the content into individual queries using ';' as delimiter
queries = file_content.split(';')

# Execute each query
for query in queries:
    # Strip whitespace and check if the query is not empty
    if query.strip():
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit changes to the database
db.commit()

# Close the cursor and the connection
cursor.close()
db.close()
