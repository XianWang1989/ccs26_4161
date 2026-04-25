
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_file = f.read()

# Split the file contents at each semicolon
queries = sql_file.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit the changes
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")

# Close the cursor and database connection
cursor.close()
db.close()
