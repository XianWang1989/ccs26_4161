
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Read the SQL file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_file = f.read()

# Split the file into individual queries
queries = sql_file.split(';')

# Execute each query
for query in queries:
    if query.strip():  # Check if the query is not empty
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
