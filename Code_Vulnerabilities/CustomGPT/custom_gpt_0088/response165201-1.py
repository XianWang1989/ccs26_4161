
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the text file containing SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the content of the file
    file_content = f.read()

    # Split the content at each ';' to get individual queries
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit changes to the database
            except Exception as e:
                print(f"Error executing query: {query}\nError: {e}")
                db.rollback()  # Rollback in case of error

# Close the cursor and connection
cursor.close()
db.close()
