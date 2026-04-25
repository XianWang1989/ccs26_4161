
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the file and read its contents
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as file:
    # Read the entire file content
    file_content = file.read()
    # Split the content at each ';' to get individual queries
    queries = file_content.split(';')

    for query in queries:
        # Strip any whitespace from the query
        cleaned_query = query.strip()
        if cleaned_query:  # Check if the query is not empty
            try:
                # Execute the cleaned query
                cursor.execute(cleaned_query)
                db.commit()  # Commit the transaction
            except MySQLdb.Error as e:
                print(f"Error executing query: {cleaned_query}")
                print(e)

# Close the cursor and the database connection
cursor.close()
db.close()
