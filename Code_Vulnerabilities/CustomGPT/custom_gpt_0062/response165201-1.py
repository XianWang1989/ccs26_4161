
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object for executing queries
cursor = db.cursor()

# Open the file containing the SQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    sql_script = file.read()  # Read the entire file

# Split the file content by ';' and remove empty queries
queries = [query.strip() for query in sql_script.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit changes for each query
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
