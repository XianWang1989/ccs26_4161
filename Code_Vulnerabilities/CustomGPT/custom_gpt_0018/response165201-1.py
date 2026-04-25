
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Open and read the file
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_file = f.read()

# Split the file content into individual queries
sql_commands = sql_file.split(';')

# Iterate over each command and execute it
for command in sql_commands:
    # Strip leading/trailing whitespace and check if it's not empty
    command = command.strip()
    if command:
        try:
            cursor.execute(command)
            db.commit()
        except MySQLdb.Error as e:
            print(f"Error executing command: {command}\nError: {e}")

# Close the cursor and connection
cursor.close()
db.close()
