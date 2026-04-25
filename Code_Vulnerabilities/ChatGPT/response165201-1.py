
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the content into queries based on the ';'
queries = file_content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Clean up leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query[:50]}... Error: {e}")

# Close the database connection
cursor.close()
db.close()
