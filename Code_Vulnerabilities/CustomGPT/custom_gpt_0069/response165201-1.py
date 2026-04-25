
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()

    # Split the content by semicolon
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit each query
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and connection
cursor.close()
db.close()
