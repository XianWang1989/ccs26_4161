
import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_contents = f.read()

# Split the file contents into individual queries by semicolon
queries = file_contents.split(';')

# Iterate over each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Avoid executing empty queries
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query[:30]}... Error: {e}")

# Commit changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
