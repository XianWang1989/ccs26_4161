
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the text file containing MySQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

    # Split the content into individual queries
    queries = content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove leading and trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit changes to the database
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
