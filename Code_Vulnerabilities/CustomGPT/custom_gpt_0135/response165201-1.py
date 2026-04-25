
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_content = f.read()

    # Split the content at each semicolon
    queries = file_content.split(';')

    # Loop through each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Only execute non-empty queries
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the changes
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
