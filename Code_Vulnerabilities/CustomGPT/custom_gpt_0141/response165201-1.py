
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file with MySQL INSERT statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()

    # Split the content into individual queries based on the semicolon
    queries = file_content.split(';')

    # Iterate over the split queries
    for query in queries:
        # Strip whitespace to avoid empty queries
        cleaned_query = query.strip()

        if cleaned_query:  # Check if the query is not empty
            try:
                # Execute the query
                cursor.execute(cleaned_query)
                # Commit the changes (optional, you can also commit after all queries)
                db.commit()
                print(f"Executed: {cleaned_query}")
            except MySQLdb.Error as e:
                # Rollback in case of error
                db.rollback()
                print(f"Error executing query: {cleaned_query}\nError: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
