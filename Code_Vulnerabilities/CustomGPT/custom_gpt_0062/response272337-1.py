
import logging

# Configure the logger
logger_sqlalchemy = {
    'level': 'INFO',
    'handlers': [],
    'qualname': 'sqlalchemy.engine'
}

# Setting up the logger
logger = logging.getLogger(logger_sqlalchemy['qualname'])
logger.setLevel(logger_sqlalchemy['level'])

# Example of adding a console handler
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# Example logging
logger.info("This is an INFO log message.")
