
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Read the file and execute queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    content = f.read()

    # Split the content by semicolon and filter out empty queries
    queries = [query.strip() for query in content.split(';') if query.strip()]

    for query in queries:
        try:
            # Execute each query
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
