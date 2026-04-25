
import logging

# Creating a logger for sqlalchemy
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Creating a console handler
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Adding the handler to the logger
logger.addHandler(handler)

# Example logging
logger.info("This is an info message.")
