
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="your_password",
                     db="test")
cursor = db.cursor()

# Read the file and execute queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()

    # Split the content by ';' and strip whitespace
    queries = [query.strip() for query in file_content.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
            db.commit()  # Commit each query if needed
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}")
            print(f"Error: {e}")

# Close the cursor and connection
cursor.close()
db.close()
