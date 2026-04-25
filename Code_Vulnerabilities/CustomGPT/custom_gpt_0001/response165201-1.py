
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object using the connection
cursor = db.cursor()

# Open the file containing SQL inserts
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file content
    file_content = f.read()

    # Split the content at each semicolon to separate the SQL queries
    queries = file_content.split(';')

    # Loop through each query
    for query in queries:
        # Strip whitespace from query to avoid empty queries
        cleaned_query = query.strip()

        # Check if cleaned_query is not empty before executing
        if cleaned_query:
            try:
                # Execute the SQL query
                cursor.execute(cleaned_query)
                # Commit the changes to the database
                db.commit()
            except MySQLdb.Error as e:
                # Print any error messages that occur
                print(f"Error executing query: {cleaned_query}\nError: {e}")
                # Rollback in case of any error
                db.rollback()

# Close the cursor and database connection
cursor.close()
db.close()
