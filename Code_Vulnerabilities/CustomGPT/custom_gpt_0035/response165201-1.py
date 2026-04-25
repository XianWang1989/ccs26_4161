
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the file content
    content = file.read()
    # Split by each ';'
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove any extraneous whitespace
        if query:  # Check if query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
