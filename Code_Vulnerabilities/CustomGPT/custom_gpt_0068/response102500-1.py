
import logging
import sys

LOG_FILENAME = '/home/me/logs/mylog.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    handlers=[
                        logging.FileHandler(LOG_FILENAME),
                        logging.StreamHandler(sys.stdout),
                    ])
