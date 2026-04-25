
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    content = file.read()

# Split queries by semicolon and remove any extra spaces
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\nError: {e}")

# Commit changes
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
