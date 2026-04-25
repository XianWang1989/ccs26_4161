
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")

with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    content = f.read()
    queries = content.split(';')

cursor = db.cursor()

for query in queries:
    query = query.strip()  # Remove leading/trailing whitespace
    if query:  # Check if query is not empty
        try:
            cursor.execute(query)
        except MySQLdb.Error as e:
            print(f"Error executing query: {e}")

db.commit()
cursor.close()
db.close()
