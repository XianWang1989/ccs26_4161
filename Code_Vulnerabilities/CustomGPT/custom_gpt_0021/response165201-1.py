
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", 
                     user="root", 
                     passwd="da66ro", 
                     db="test")
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the content at each semicolon
queries = file_content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Ensure the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit changes for each successful query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
