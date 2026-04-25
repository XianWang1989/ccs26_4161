
import MySQLdb

# Establish database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Open the file containing MySQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file contents
    file_content = f.read()
    # Split the content by ';' to get individual queries
    queries = file_content.split(';')

    for query in queries:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)  # Execute the query
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}\n{e}")

# Close the cursor and connection
cursor.close()
db.close()
