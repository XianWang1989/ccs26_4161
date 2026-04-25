
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Read the file and execute each query
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    content = f.read()

    # Split the content by ';' and iterate over each query
    queries = content.split(';')
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Skip empty queries
            try:
                cursor.execute(query)  # Execute the query
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Commit changes to the database
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
