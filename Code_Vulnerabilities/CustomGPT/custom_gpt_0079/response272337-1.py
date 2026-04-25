
import logging
from sqlalchemy import create_engine
from pyramid.config import Configurator

# Setting up logging
logging.config.fileConfig('your_config.ini')

# Example of creating an SQLAlchemy engine
engine = create_engine('sqlite:///example.db')

# Now, when SQLAlchemy logs messages, it will use the settings defined in your_config.ini
