
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the content by semicolon and filter out any empty queries
    queries = [query.strip() for query in file_content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")
            db.rollback()  # Rollback in case of error

# Close the cursor and connection
cursor.close()
db.close()
