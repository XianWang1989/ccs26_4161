
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_file = f.read()

# Split the file content into individual queries
queries = sql_file.split(';')

# Iterate through the queries and execute them
for query in queries:
    query = query.strip()  # Clean up any extra whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and connection
cursor.close()
db.close()
