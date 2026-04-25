
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file containing MySQL insert statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    content = f.read()

    # Split the content by the semicolon delimiter
    queries = content.split(';')

    # Loop through each query and execute it
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit the transaction
            except Exception as e:
                print(f"Error executing query: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
