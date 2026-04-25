
import logging

logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()  # or any other handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('This is an info message for SQLAlchemy.')
