
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Read the file and execute queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    content = f.read()

# Split queries by ';' and strip whitespace
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit the transaction for each query
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}. Error: {e}")

# Close cursor and database connection
cursor.close()
db.close()
