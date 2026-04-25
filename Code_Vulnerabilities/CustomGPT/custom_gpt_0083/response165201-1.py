
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file and read it
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()

# Split the content by semicolon and remove any extra whitespace
queries = [query.strip() for query in file_content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit changes if the query modifies data
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
