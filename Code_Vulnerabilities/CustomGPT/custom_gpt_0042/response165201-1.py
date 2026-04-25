
import MySQLdb

def execute_queries_from_file(file_path):
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="da66ro",
                         db="test")

    cursor = db.cursor()

    try:
        # Open the file and read its content
        with open(file_path, 'r') as file:
            # Read the entire file
            content = file.read()

            # Split the content at each ';'
            queries = content.split(';')

            # Iterate over the queries and execute each one
            for query in queries:
                query = query.strip()  # Remove leading/trailing whitespace
                if query:  # Ensure the query is not empty
                    cursor.execute(query)

        # Commit the changes
        db.commit()

    except MySQLdb.Error as e:
        print(f"Error occurred: {e}")

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

# Specify the file path
file_path = 'E:/estudos/projetos/tricae/tests_python.txt'
execute_queries_from_file(file_path)
