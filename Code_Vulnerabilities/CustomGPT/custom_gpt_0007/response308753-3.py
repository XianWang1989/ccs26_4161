
import time
import logging

logger = logging.getLogger(__name__)

def log_sql_execution():
    query = "SELECT TIMESTAMPDIFF(...) AS 'duration', ..."
    start_time = time.time()
    raw_data = dbs.executesql(query, as_dict=True)
    execution_time = time.time() - start_time
    logger.info(f"Executed SQL in {execution_time} seconds")
    return raw_data
