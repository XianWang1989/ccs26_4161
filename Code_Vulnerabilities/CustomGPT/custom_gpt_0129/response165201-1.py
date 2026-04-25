
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the content by semicolons to separate each query
    queries = file_content.split(';')

    # Iterate over each query
    for query in queries:
        # Strip whitespace to avoid issues with empty queries
        query = query.strip()
        if query:  # Ensure not to execute empty queries
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
