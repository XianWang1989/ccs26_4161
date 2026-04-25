
import time
from gluon import current

def exec_sql_with_timing(query):
    db = current.db
    start_time = time.time()
    result = db.executesql(query, as_dict=True)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.4f} seconds")
    return result

def test_queries():
    query = """
    SELECT TIMESTAMPDIFF(...) AS 'duration', 
           <other_columns>
    FROM <your_table> AS ris 
    JOIN <other_table> as sd on ris.id = sd.id
    WHERE ris.datetime_column != '0000-00-00 00:00:00' 
      AND ris.datetime_column >= '2010-08-15' 
      AND ris.datetime_column <= '2014-08-22'
    """

    # Testing in a web request context
    raw_data = exec_sql_with_timing(query)

    # You can also test using the debug console with:
    # from gluon.debug import dbg
    # dbg.set_trace()
    # raw_data = exec_sql_with_timing(query)

# Call the function in your controller or any part of your application
test_queries()
