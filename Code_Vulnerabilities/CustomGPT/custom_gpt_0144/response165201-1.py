import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

# Read and split the file by semicolons
with open('E:/estudos/projetos/tricae/tests_python.txt', 'r', encoding='utf-8') as f:
    sql_file = f.read()

# Split queries by semicolon
sql_commands = sql_file.strip().split(';')

# Execute each query
for command in sql_commands:
    command = command.strip()
    if command:
        try:
            cursor.execute(command)
        except Exception as e:
            print(f"Error executing query: {command}\n{e}")

# Commit and close the connection
db.commit()
cursor.close()
db.close()
