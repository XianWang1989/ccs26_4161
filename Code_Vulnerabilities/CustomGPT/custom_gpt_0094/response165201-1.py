
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="your_password",
                     db="test")

# Create a cursor object
cursor = db.cursor()

# Open the text file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    # Read the entire file
    content = f.read()

# Split the content at each semicolon
queries = content.split(';')

# Execute each query
for query in queries:
    query = query.strip()  # Remove any leading/trailing whitespace
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)  # Execute the query
            db.commit()  # Commit the transaction
        except Exception as e:
            print(f"An error occurred: {e}")

# Close the cursor and database connection
cursor.close()
db.close()
