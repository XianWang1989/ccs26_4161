
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    file_content = file.read()

# Split the content by ';' and filter empty queries
queries = [query.strip() for query in file_content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\n{e}")

# Close the cursor and connection
cursor.close()
db.close()
