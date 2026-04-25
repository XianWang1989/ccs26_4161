
import logging
import logging.config
import pathlib

# Example of an INI-like configuration
config = """
[loggers]
keys=root,sqlalchemy

[handlers]
keys=consoleHandler

[formatters]
keys=defaultFormatter

[logger_sqlalchemy]
level = INFO
handlers = consoleHandler
qualname = sqlalchemy.engine

[handler_consoleHandler]
class = StreamHandler
level = DEBUG
formatter = defaultFormatter
args = []

[formatter_defaultFormatter]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
"""

# Parse the configuration string
logging.config.fileConfig(pathlib.Path("path/to/your/config.ini"), disable_existing_loggers=False)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message")
