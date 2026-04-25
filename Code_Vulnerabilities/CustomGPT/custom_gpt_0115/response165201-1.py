
import MySQLdb

# Establish the database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    file_content = f.read()

    # Split the content by ';' to get individual queries
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}. Error: {e}")

# Close the cursor and connection
cursor.close()
db.close()
