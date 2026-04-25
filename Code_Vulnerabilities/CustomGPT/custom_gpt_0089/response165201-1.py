
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    data = f.read()

# Split the content at each ';' to get individual queries
queries = data.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
