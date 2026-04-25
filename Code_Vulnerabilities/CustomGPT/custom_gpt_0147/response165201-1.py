
import MySQLdb

# Step 1: Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Step 2: Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Step 3: Split the content at each semicolon
queries = content.split(';')

# Step 4: Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}")
            print(f"MySQL Error {e.args[0]}: {e.args[1]}")

# Step 5: Clean up
cursor.close()
db.close()
