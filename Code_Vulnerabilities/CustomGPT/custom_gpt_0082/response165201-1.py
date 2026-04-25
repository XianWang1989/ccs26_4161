
import MySQLdb

# Database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Function to read file and execute queries
def execute_queries_from_file(file_path):
    with open(file_path, 'r') as f:
        # Read the whole file content
        file_content = f.read()

        # Split content by ';' and filter out empty statements
        queries = [query.strip() for query in file_content.split(';') if query.strip()]

        for query in queries:
            try:
                # Execute the SQL query
                cursor.execute(query)

                # Optional: commit after each query if needed
                db.commit()

            except MySQLdb.Error as e:
                print(f"Error executing query: {query}. Error: {e}")
                db.rollback()  # Rollback in case of error

# Path to your text file
file_path = 'E:/estudos/projetos/tricae/tests_python.txt'
execute_queries_from_file(file_path)

# Close cursor and database connection
cursor.close()
db.close()
