
import logging
import os

LOG_DIRECTORY = '/home/me/logs'
LOG_FILENAME = 'mylog.txt'
os.makedirs(LOG_DIRECTORY, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIRECTORY, LOG_FILENAME),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
