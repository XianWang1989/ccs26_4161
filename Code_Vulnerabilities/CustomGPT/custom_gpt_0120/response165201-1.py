
import MySQLdb

# Establish the database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Open the text file containing the SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_queries = f.read().split(';')  # Split by ';'

# Execute each query
for query in sql_queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            db.commit()  # Commit the transaction for each query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}\n{e}")

# Close the database connection
cursor.close()
db.close()
