
from gluon import current
from gluon.debug import dbg

db = current.db

def execute_queries():
    # Example query (replace with your actual query)
    query = """
        SELECT TIMESTAMPDIFF(...) AS 'duration',
               ...
        FROM your_table AS ris
        JOIN another_table AS sd ON ris.id = sd.id
        WHERE ris.odate != '0000-00-00 00:00:00'
          AND ris.odate >= '2010-08-15'
          AND ris.odate <= '2014-08-22'
    """

    # Check if connection pooling is enabled
    if not db._uri:  # or however you check your pooling
        db.connect()  # Connect if not already connected

    raw_data = db.executesql(query, as_dict=True)
    print(raw_data)

    # If necessary, use caching
    # cache_query_results(query)

# Run the function
execute_queries()
