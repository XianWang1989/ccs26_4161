
import MySQLdb

# Connect to MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

cursor = db.cursor()

# Open the file with MySQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire content of the file
    content = f.read()

    # Split the content into individual queries
    queries = content.split(';')

    for query in queries:
        # Strip whitespace from the query
        query = query.strip()

        # Skip empty queries
        if query:
            try:
                # Execute the query
                cursor.execute(query)
                # You can commit here if needed
                # db.commit()
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}\nError: {e}")

# Close the cursor and the connection
cursor.close()
db.close()
