
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the text file containing the SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_file = f.read()  # Read the entire file

# Split the file content into individual queries
queries = sql_file.split(';')

# Iterate over each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Execute non-empty queries only
        try:
            cursor.execute(query)  # Execute the query
            print(f"Executed: {query}")
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")

# Commit changes to the database
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
