
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Read the file and execute queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the content at each ';', filtering out empty strings
queries = [query.strip() for query in file_content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query + ';')  # Add semicolon back for execution
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
