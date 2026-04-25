
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file and read lines
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

# Split the file content at each ';' and strip whitespace
queries = [query.strip() for query in file_content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)  # Execute the query
        db.commit()  # Commit the changes
    except MySQLdb.Error as e:
        print(f"Error executing query: {query[:30]}... - {e}")

# Close the cursor and database connection
cursor.close()
db.close()
