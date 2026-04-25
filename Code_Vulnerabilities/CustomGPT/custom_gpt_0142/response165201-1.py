
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file containing MySQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file content
    file_content = f.read()

    # Split the content into individual queries using ';' as the delimiter
    queries = file_content.split(';')

    # Execute each query
    for query in queries:
        # Strip leading and trailing whitespace and check if not empty
        cleaned_query = query.strip()
        if cleaned_query:
            try:
                cursor.execute(cleaned_query)
                print(f"Executed query: {cleaned_query}")
            except MySQLdb.Error as e:
                print(f"Error executing query: {cleaned_query}\nError: {e}")

# Commit the changes if needed
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
