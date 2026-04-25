
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    content = f.read()

    # Split the content into individual queries using ';' as the delimiter
    queries = content.split(';')

    # Loop through each query
    for query in queries:
        # Strip whitespace and ensure the query isn't empty
        query = query.strip()
        if query:
            try:
                # Execute the query
                cursor.execute(query)
                # Commit the transaction (if needed - depends on your use case)
                db.commit()
            except MySQLdb.Error as e:
                # Print error message if the query fails
                print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
