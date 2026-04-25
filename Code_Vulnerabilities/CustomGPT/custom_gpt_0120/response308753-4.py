
from gluon import DAL

# Connection setup
db = DAL('mysql://user:password@localhost/dbname', pool_size=10)

# Define the query
query = """
SELECT TIMESTAMPDIFF(...) AS 'duration', ... 
FROM ... AS ris 
JOIN ... as sd ON ris.... = sd....
WHERE ris.... != '0000-00-00 00:00:00' 
AND ris.... >= '2010-8-15' 
AND ris.... <= '2014-8-22'
"""

# Execute query with logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def execute_query(query):
    logger.debug(f"Executing query: {query}")
    return db.executesql(query, as_dict=True)

# Call the function
raw_data = execute_query(query)
