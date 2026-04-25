
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    file_content = f.read()

    # Split the content by ';' and remove any extra whitespace
    queries = [query.strip() for query in file_content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit changes if applicable
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}")
            print(f"Error message: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
