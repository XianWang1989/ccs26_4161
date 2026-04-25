
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Split the content at each ';' and remove any leading/trailing whitespace
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit the transaction
    except MySQLdb.Error as e:
        print(f"Error executing query: {query} - Error: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
