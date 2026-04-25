
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Cursor to execute queries
cursor = db.cursor()

# Reading the file and executing queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()

# Splitting the content by the semicolon and filtering out empty queries
queries = [query.strip() for query in content.split(';') if query.strip()]

# Executing each query
for query in queries:
    try:
        cursor.execute(query)
        db.commit()  # Commit each query after execution
    except Exception as e:
        db.rollback()  # Rollback in case of error
        print(f"Error executing query: {query}\n{e}")

# Closing the cursor and connection
cursor.close()
db.close()
