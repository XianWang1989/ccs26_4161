
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file in read mode
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file contents
    file_contents = f.read()

    # Split the contents into individual queries based on ';'
    queries = file_contents.split(';')

    # Iterate through each query
    for query in queries:
        # Strip whitespace and check if the query is not empty
        query = query.strip()
        if query:
            try:
                # Execute the query
                cursor.execute(query)
                # Commit the transaction (if applicable)
                db.commit()
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}\nError: {e}")
                db.rollback()  # Rollback in case of error

# Close the cursor and database connection
cursor.close()
db.close()
