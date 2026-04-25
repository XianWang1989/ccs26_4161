
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object using the db connection
cursor = db.cursor()

# Open the file containing SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the file content
    content = file.read()

    # Split the content at each semicolon
    queries = content.split(';')

    # Loop through each query and execute it if it is not empty
    for query in queries:
        query = query.strip()  # Remove leading and trailing whitespace
        if query:  # Only execute non-empty queries
            try:
                cursor.execute(query)
                print(f"Executed query: {query}")
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}")
                print(f"MySQL Error: {e}")

# Commit the transactions
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
