
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    content = file.read()

    # Split the content at each semicolon
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Execute only if the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit the transaction
            except Exception as e:
                print(f"An error occurred: {e}")
                db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
