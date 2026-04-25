
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    file_content = f.read()

# Split the file content by ';' to get individual queries
queries = file_content.split(';')

# Iterate over each query and execute it
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}. Error: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
