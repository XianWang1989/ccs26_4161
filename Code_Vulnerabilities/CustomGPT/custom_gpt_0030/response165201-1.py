
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="da66ro",
    db="test"
)

# Prepare a cursor object using the cursor() method
cursor = db.cursor()

# Read the SQL file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    content = file.read()

# Split the content by semicolon and strip whitespace
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
    except MySQLdb.Error as e:
        print(f"Error occurred: {e}")

# Commit the changes to the database
db.commit()

# Close the cursor and the database connection
cursor.close()
db.close()
