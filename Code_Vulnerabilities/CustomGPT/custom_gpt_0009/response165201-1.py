
import MySQLdb

# Connect to MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Split the content into individual SQL queries
queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the changes
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
