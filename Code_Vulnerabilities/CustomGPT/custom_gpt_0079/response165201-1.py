
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read file content
    sql_script = f.read()

# Split the script at each ';' and execute each query
queries = sql_script.split(';')

for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the changes if needed
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}. Error: {e}")

# Close the cursor and the connection
cursor.close()
db.close()
