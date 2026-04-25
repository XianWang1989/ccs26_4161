
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the content into individual queries
queries = file_content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")

# Commit the transaction
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
