
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
    # Read the entire file
    file_content = f.read()

# Split the file content into individual queries
queries = file_content.split(';')

# Iterate over each query and execute it
for query in queries:
    query = query.strip()  # Remove whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
