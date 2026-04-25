
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file containing the SQL insert statements
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    sql_file = file.read()

# Split the content by semicolon and remove any whitespace
queries = [query.strip() for query in sql_file.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit the transaction for each successful query
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
