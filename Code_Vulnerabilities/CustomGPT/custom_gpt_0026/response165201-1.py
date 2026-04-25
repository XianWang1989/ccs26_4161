
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="your_password",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    data = f.read()
    # Split the data into individual queries
    queries = data.split(';')

    # Iterate through each query and execute it
    for query in queries:
        query = query.strip()  # Remove any leading/trailing whitespace
        if query:  # Check if the query is not empty
            try:
                cursor.execute(query)
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {query}")
                print(f"MySQL Error: {e}")
                db.rollback()  # Rollback in case of error

# Close the cursor and the database connection
cursor.close()
db.close()
