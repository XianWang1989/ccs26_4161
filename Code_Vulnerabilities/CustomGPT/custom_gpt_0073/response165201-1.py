
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Read the file and execute queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()
    # Split the content at each semicolon
    queries = file_content.split(';')

    # Iterate through each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Ensure it's not an empty string
            try:
                cursor.execute(query)  # Execute the query
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
