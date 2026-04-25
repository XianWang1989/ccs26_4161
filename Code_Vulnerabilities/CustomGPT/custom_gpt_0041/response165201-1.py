
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Open the text file containing MySQL insert statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the file content
    file_content = file.read()

# Split the content into individual queries
queries = file_content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading or trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
