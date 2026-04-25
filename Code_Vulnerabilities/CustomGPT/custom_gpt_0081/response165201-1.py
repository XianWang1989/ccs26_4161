
import MySQLdb

# Establish the database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    contents = f.read()

# Split the contents by the delimiter ';' and strip any whitespace
queries = [query.strip() for query in contents.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit the transaction for each query
    except MySQLdb.Error as e:
        print(f"Error executing query: {query[:50]}... Error: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
