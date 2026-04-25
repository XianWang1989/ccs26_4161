
# Assuming you have your web2py environment set up correctly

from gluon import current, redirect, URL

def my_function():
    db = current.db
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               TIMESTAMPDIFF(...) - INTERVAL 1 HOUR,
               ris.ODATE as 'date',
               CONCAT(...) as 'service'
        FROM ... AS ris
        JOIN ... as sd ON ris... = sd...
        WHERE ris... != '0000-00-00 00:00:00'
            AND ris.... >= '2010-8-15'
            AND ris.... <= '2014-8-22'
    """

    # Measure time manually to check performance
    import time
    start_time = time.time()
    raw_data = db.executesql(query, as_dict=True)
    print("Execution Time: {:.2f} seconds".format(time.time() - start_time))

    return raw_data
