
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Open the file and read the contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_script = f.read()

# Split the script at each ';' to separate individual queries
queries = sql_script.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading or trailing whitespace
    if query:  # Only execute non-empty queries
        try:
            cursor.execute(query)
            db.commit()  # Commit after each query
        except MySQLdb.Error as e:
            print(f"Error executing query: {query}")
            print(e)

# Close the cursor and database connection
cursor.close()
db.close()
