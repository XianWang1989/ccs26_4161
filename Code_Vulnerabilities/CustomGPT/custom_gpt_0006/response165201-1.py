
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file with MySQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()

# Split the content by semicolon, filtering out empty queries
queries = [query.strip() for query in content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit changes for each query
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Rollback in case of error

# Close the cursor and database connection
cursor.close()
db.close()
