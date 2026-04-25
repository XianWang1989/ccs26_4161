
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire content and split by ';'
    queries = file.read().strip().split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit changes to the database
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()
