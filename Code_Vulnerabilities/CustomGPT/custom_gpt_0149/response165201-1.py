
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file contents
    file_contents = f.read()

    # Split the contents into queries
    queries = file_contents.split(';')

    # Iterate over each query
    for query in queries:
        query = query.strip()  # Remove any extra whitespace
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the transaction
            except Exception as e:
                print(f"An error occurred: {e}")  # Handle any errors
                db.rollback()  # Rollback in case of an error

# Close the cursor and database connection
cursor.close()
db.close()
