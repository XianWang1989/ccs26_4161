
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open the text file containing the MySQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the file contents
    file_contents = f.read()

    # Split the contents at each ';' to get individual queries
    queries = file_contents.split(';')

    # Loop through each query
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                # Execute the query
                cursor.execute(query)
                db.commit()  # Commit changes
            except MySQLdb.Error as e:
                print(f"Error executing query: {e}")
                db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
