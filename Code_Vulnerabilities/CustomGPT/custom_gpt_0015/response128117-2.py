
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Database path: %s", app.config['DATABASE'])
