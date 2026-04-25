
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file containing the SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    sql_file = f.read()

    # Split the file by ';' and remove any extra whitespace
    queries = [query.strip() for query in sql_file.split(';') if query.strip()]

    # Execute each query
    for query in queries:
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

# Commit the changes
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
