
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Open the file for reading
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the content by semicolon
    queries = file_content.split(';')

    # Iterate over each query
    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Only execute if query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit changes
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")
                db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
