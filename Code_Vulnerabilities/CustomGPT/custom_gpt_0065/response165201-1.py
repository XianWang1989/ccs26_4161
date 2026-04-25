
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Open the file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    file_content = file.read()

# Split the content into individual queries
queries = file_content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit each query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")

# Close the cursor and database connection
cursor.close()
db.close()
