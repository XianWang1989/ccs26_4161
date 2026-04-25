
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="da66ro", db="test")
cursor = db.cursor()

with open('E:/estudos/projetos/tricae/tests_python.txt', 'r') as f:
    sql_script = f.read()
    queries = sql_script.split(';')

for query in queries:
    query = query.strip()
    if query:  # Check if the query is not empty
        try:
            cursor.execute(query)
            print(f'Executed: {query}')
        except MySQLdb.Error as e:
            print(f'Error executing query: {e}')

db.commit()
cursor.close()
db.close()
