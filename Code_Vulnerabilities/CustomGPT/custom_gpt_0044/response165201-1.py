
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()

# Split the content at each ';' to get individual queries
queries = file_content.split(';')

# Iterate through each query and execute it
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and connection
cursor.close()
db.close()
