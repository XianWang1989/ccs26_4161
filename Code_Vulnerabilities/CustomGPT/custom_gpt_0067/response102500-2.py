
import os

if os.environ.get('SERVER_SOFTWARE', '').startswith('Development'):
    LOG_FILENAME = '/home/me/logs/mylog.txt'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG) 
