
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Read the file and execute the queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()  # Read the entire file content
    queries = content.split(';')  # Split the content by semicolon

    for query in queries:
        query = query.strip()  # Remove leading and trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
