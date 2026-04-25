
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read file content
    content = f.read()

    # Split queries at each ';' and remove any extra whitespace
    queries = [query.strip() for query in content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit each query if it's successfully executed
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")
            db.rollback()  # Rollback on error

# Close the cursor and database connection
cursor.close()
db.close()
