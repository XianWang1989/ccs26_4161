
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()

    # Split the content by semicolon and strip whitespace
    queries = [query.strip() for query in content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit changes if the query modifies the database
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}. Error: {e}")

# Close the cursor and connection
cursor.close()
db.close()
