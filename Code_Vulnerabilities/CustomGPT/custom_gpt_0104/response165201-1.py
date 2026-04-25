
import MySQLdb

# Establish the database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the text file containing MySQL insert statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    file_content = f.read()  # Read the entire file content
    queries = file_content.split(';')  # Split the content at each semicolon

    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                print("Executed: ", query)  # Print the executed query for confirmation
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")  # Handle any errors

# Commit the changes and close the connection
db.commit()
cursor.close()
db.close()
