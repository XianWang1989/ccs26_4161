
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Split the content by ';' and strip whitespace from each query
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit the transaction for each query
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\n{e}")
        db.rollback()  # Rollback in case of an error

# Close the cursor and the database connection
cursor.close()
db.close()
