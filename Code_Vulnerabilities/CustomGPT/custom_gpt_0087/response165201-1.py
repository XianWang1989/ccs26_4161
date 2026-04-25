
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the file containing MySQL insert statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the content by the semicolon to get individual queries
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        # Remove leading/trailing whitespace
        cleaned_query = query.strip()
        if cleaned_query:  # Ensure it's not an empty string
            try:
                cursor.execute(cleaned_query)  # Execute the query
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {cleaned_query}\n{e}")

# Close the cursor and the database connection
cursor.close()
db.close()
