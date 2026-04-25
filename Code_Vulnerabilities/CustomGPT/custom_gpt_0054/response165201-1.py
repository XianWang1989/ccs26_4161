
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    file_contents = file.read()

# Split the contents at each ';' to get individual queries
queries = file_contents.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
