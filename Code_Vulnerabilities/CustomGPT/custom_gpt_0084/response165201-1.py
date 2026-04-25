
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    file_content = f.read()

    # Split the content by semicolon and filter out empty queries
    queries = [query.strip() for query in file_content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit changes
        except Exception as e:
            print(f"Error executing query: {query}\nError: {e}")
            db.rollback()  # Rollback on error

# Close the cursor and database connection
cursor.close()
db.close()
