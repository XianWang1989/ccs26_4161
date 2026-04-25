
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file containing SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file into a string
    content = f.read()

    # Split the content at each semicolon and remove empty strings
    queries = [query.strip() for query in content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {query} \nError: {e}")
            db.rollback()  # Rollback if there's an error

# Close the cursor and database connection
cursor.close()
db.close()
