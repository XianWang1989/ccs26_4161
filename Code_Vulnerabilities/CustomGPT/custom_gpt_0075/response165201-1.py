
import MySQLdb

# Establish the database connection
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="da66ro",
                     db="test")
cursor = db.cursor()

# Function to execute queries from the file
def execute_queries_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            query = ""
            for line in f:
                # Append the line to the query
                query += line.strip()
                # Execute the query if a semicolon is found
                if query.endswith(';'):
                    cursor.execute(query[:-1])  # Remove the last ';' before executing
                    query = ""  # Reset query

        # Commit the changes
        db.commit()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        db.rollback()

    finally:
        cursor.close()
        db.close()

# Call the function with the path to the file
execute_queries_from_file('E:/estudos/projetos/tricae/tests_python.txt')
