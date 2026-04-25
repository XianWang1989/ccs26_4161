
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file for reading
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_script = f.read()  # Read the entire file content

# Split the file content at each ';' to get individual queries
queries = sql_script.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes to the database
db.commit()

# Clean up
cursor.close()
db.close()
