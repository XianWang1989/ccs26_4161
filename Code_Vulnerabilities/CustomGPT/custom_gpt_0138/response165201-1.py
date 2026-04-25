
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()

    # Split the content by semicolon
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        # Strip whitespace from the query
        query = query.strip()
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit changes
            except MySQLdb.Error as e:
                print(f"Error executing query: {query} - {e}")

# Close the cursor and connection
cursor.close()
db.close()
