
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file containing the SQL insert statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    content = f.read()

# Split the content at each semicolon to extract individual queries
queries = content.split(';')

# Iterate over each query
for query in queries:
    # Strip leading/trailing whitespace
    query = query.strip()

    # Execute the query if it's not empty
    if query:
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
