
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="your_password", db="test")
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_content = f.read()

    # Split the content by ';' to get individual queries
    queries = file_content.split(';')

    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Ensure the query is not empty
            try:
                cursor.execute(query)  # Execute the query
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")  # Handle any errors

# Commit the changes to the database
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()
