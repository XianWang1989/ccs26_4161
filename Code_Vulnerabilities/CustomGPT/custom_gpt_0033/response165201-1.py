
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Read the file and execute each query
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()

# Split content by ';' and strip any whitespace
queries = [query.strip() for query in file_content.split(';') if query.strip()]

# Execute each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit changes for each query
    except MySQLdb.Error as e:
        print(f"Error executing query: {query}\n{e}")

# Close the cursor and database connection
cursor.close()
db.close()
