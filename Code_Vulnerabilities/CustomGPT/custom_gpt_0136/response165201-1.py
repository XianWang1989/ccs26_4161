
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    data = f.read()

# Split the content by ';' to get individual queries
queries = data.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove extra whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
