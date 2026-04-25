
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the file content at each ';' to get individual queries
queries = file_content.split(';')

# Loop through each query, execute it, and commit if it's valid
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not an empty string
        try:
            cursor.execute(query)
            db.commit()  # Commit the changes to the database
            print(f"Executed query: {query[:30]}...")  # Print a snippet of the query for verification
        except MySQLdb.Error as e:
            print(f"Error executing query: {query[:30]}... - Error: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
