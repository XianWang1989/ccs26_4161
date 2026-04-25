
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()
    # Split the content by the semicolon ';'
    queries = file_content.split(';')

    # Iterate through each query
    for query in queries:
        # Strip whitespace and check if the query is not empty
        if query.strip():
            try:
                # Execute the query
                cursor.execute(query)
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Commit changes to the database
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()
