
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Read the file and execute each query
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_content = f.read()

    # Split the content at each semicolon
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
