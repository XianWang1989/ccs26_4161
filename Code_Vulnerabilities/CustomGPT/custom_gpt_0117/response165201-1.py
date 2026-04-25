
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file containing the SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()

    # Split the content at each semicolon to get individual queries
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Commit the transactions
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
