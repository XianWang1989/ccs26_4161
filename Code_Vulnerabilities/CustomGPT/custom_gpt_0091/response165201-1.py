
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file
    file_contents = file.read()

    # Split the contents at each semicolon
    queries = file_contents.split(';')

    # Iterate over each query
    for query in queries:
        # Strip whitespace and ensure the query is not empty
        query = query.strip()
        if query:
            try:
                # Execute the query
                cursor.execute(query)
                db.commit()  # Commit changes for each successful query
            except Exception as e:
                print(f"Error executing query: {e}")

# Close the cursor and connection
cursor.close()
db.close()
