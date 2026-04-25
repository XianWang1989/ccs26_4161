
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    content = f.read()

    # Split the content at each semicolon
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit the transaction
            except Exception as e:
                print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and connection
cursor.close()
db.close()
