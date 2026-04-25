
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object using the cursor() method
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    file_content = f.read()

    # Split the content into individual queries
    queries = file_content.split(';')

    # Iterate through each query
    for query in queries:
        # Strip whitespace and check if the query is not empty
        query = query.strip()
        if query:  # Only execute non-empty queries
            try:
                # Execute the query
                cursor.execute(query)
                # Commit the changes
                db.commit()
            except MySQLdb.Error as e:
                # Rollback in case there is any error
                print(f"Error: {e}")
                db.rollback()

# Close the cursor and database connection
cursor.close()
db.close()
