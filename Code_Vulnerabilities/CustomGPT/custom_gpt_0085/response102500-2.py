
import os
import logging

LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logs', 'mylog.txt')
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# Check if the log directory is writable
if not os.path.exists(os.path.dirname(LOG_FILENAME)):
    os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)
