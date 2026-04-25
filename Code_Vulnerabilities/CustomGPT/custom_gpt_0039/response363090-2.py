
from django.db import connection

def regex_function():
    cursor = connection.cursor()
    cursor.execute("CREATE FUNCTION regexp(pattern TEXT, value TEXT) RETURNS INTEGER AS $$ "
                   "SELECT CASE WHEN value ~ pattern THEN 1 ELSE 0 END; $$ LANGUAGE sql;")
    cursor.close()

# Call this function after your database connection is ready
