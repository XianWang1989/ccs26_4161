
LOG_FILENAME = '/home/me/logs/mylog.txt'

# Make sure the directory exists
import os
if not os.path.exists(os.path.dirname(LOG_FILENAME)):
    os.makedirs(os.path.dirname(LOG_FILENAME))

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# Now logging should work as intended
