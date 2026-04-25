
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="your_password",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Split the content into individual queries
queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Only execute non-empty queries
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
