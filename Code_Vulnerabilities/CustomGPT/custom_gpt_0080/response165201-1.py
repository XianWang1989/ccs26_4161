
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_content = f.read()

    # Split the content into individual queries
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Avoid executing empty queries
            try:
                cursor.execute(query)
                print(f"Executed query: {query}")
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")

# Commit changes to the database (if any)
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
