
import MySQLdb

# Establish the database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the text file and read its content
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Split the content by ';' to get individual queries
queries = content.split(';')

# Loop through each query and execute it
for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit each query if successful
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")
            db.rollback()  # Rollback if there is an error

# Close the cursor and database connection
cursor.close()
db.close()
