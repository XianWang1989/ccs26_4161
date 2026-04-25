
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the content into separate queries
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Skip empty queries
            try:
                cursor.execute(query)  # Execute the query
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Commit changes if any INSERT/UPDATE/DELETE queries were executed
db.commit()

# Close the database connection
cursor.close()
db.close()
