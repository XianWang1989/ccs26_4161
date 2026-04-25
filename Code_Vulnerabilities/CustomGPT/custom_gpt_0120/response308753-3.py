
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def execute_query(query):
    logger.debug(f"Executing query: {query}")
    return db.executesql(query, as_dict=True)
