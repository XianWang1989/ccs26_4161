
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file containing SQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_script = f.read()

# Split the script into individual queries
queries = sql_script.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Ensure it's not an empty query
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
