
import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

# Create a cursor object to execute queries
cursor = db.cursor()

# Read the file and execute queries
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_commands = f.read().strip().split(';')  # Split by semicolon

    for command in sql_commands:
        command = command.strip()  # Remove any leading/trailing whitespace
        if command:  # Check if the command is not empty
            try:
                cursor.execute(command)  # Execute the SQL command
            except MySQLdb.Error as e:
                print(f"Error executing command: {e}")

# Commit the transaction to save changes
db.commit()

# Close the cursor and connection
cursor.close()
db.close()
