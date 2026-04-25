
import logging
import os

LOG_FILENAME = os.path.join(os.path.expanduser('~'), 'logs', 'mylog.txt')
os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# Your existing handlers here...
