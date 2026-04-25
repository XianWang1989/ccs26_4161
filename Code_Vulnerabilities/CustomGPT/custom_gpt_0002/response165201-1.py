
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Read the file and execute each query
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    queries = f.read().strip().split(';')  # Split the content by ';'

    for query in queries:
        query = query.strip()  # Clean up whitespace
        if query:  # Check if the query is not empty
            cursor.execute(query)

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
