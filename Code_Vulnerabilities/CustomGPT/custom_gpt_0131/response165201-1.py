
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file containing MySQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the file's content
    content = file.read()

# Split the content at each semicolon (';')
queries = content.split(';')

# Execute each query
for query in queries:
    # Strip whitespace to avoid errors
    query = query.strip()
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            print(f"Executed query: {query}")
        except MySQLdb.Error as err:
            print(f"Error: {err}")

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
