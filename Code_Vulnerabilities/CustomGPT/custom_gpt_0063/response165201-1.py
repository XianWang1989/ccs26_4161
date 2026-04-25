
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    data = file.read()

# Split the data at each ';' and filter out any empty strings
queries = [query.strip() for query in data.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit after each query or at the end
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and the database connection
cursor.close()
db.close()
