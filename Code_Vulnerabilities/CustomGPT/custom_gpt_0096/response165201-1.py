
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Read the file and split queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()
    queries = file_content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}")
            print(e)

# Close the cursor and connection
cursor.close()
db.close()
