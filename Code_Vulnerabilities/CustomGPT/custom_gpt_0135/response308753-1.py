
# Optimize connection pooling settings
db = DAL('mysql://username:password@localhost/dbname', pool_size=10, check_reserved=['all'])

# Example of executing multiple queries more efficiently
def execute_queries():
    query = """
    SELECT TIMESTAMPDIFF(...), ODATE AS 'date', CONCAT(...) AS 'service'
    FROM ... AS ris
    JOIN ... as sd ON ris.id = sd.id
    WHERE ris.ODATE IS NOT NULL
    AND ris.ODATE BETWEEN '2010-08-15' AND '2014-08-22'
    """

    # Execute a batch of queries
    with db.transaction():
        raw_data_1 = db.executesql(query, as_dict=True)
        raw_data_2 = db.executesql(query, as_dict=True)
        raw_data_3 = db.executesql(query, as_dict=True)

    return raw_data_1, raw_data_2, raw_data_3

# Invoke the function
data = execute_queries()
