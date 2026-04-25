
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file containing the MySQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()

# Split the content by semicolon and strip any extra whitespace
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit the transaction for each executed query
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
