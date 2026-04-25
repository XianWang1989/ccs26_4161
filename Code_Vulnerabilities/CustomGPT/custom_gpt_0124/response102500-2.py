
import os

LOG_FILENAME = '/home/me/logs/mylog.txt' if os.environ.get('GAE_ENV') is None else None
if LOG_FILENAME:
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.DEBUG)
