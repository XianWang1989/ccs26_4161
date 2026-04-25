
import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    data = f.read()

# Split the data into individual queries
queries = data.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes after each query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
