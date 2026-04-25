
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()
    # Split the content by ';'
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove any leading or trailing whitespace
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}")
                print(f"MySQL Error: {e}")

# Close cursor and connection
cursor.close()
db.close()
