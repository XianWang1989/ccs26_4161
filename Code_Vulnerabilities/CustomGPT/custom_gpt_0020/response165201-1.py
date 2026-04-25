
import MySQLdb

# Establish a connection to the database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file containing the SQL queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the contents at each semicolon to get individual queries
    queries = file_content.split(';')

    # Iterate through each query
    for query in queries:
        # Strip any leading/trailing whitespace
        sql = query.strip()

        # Check if the sql command is not empty
        if sql:
            try:
                # Execute the SQL query
                cursor.execute(sql)
                # Commit the transaction
                db.commit()
            except MySQLdb.Error as e:
                # Print error if the query fails and rollback the transaction
                print(f"An error occurred: {e}")
                db.rollback()

# Close the cursor and database connection
cursor.close()
db.close()
