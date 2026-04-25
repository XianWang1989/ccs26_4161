
import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    content = file.read()

    # Split the content at each ';' to separate the queries
    queries = content.split(';')

    # Iterate over each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
