
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    file_content = f.read()

    # Split the content by ';' to extract each query
    queries = file_content.split(';')

    # Iterate through each query and execute it
    for query in queries:
        query = query.strip()  # Remove any leading or trailing whitespace
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit changes
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")  # Print any errors

# Close the cursor and database connection
cursor.close()
db.close()
