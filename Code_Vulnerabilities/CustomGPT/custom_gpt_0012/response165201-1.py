
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    sql_file = f.read()

# Split the file by ';' and clean up extra whitespace
queries = [query.strip() for query in sql_file.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit each query
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Rollback in case of error

# Close the cursor and database connection
cursor.close()
db.close()
