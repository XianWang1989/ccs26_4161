
import logging
import google.cloud.logging
from google.cloud.logging import DESCENDING

# Initialize Cloud Logging
client = google.cloud.logging.Client()
client.setup_logging()

# Use the logger
logging.debug('Debug message for Cloud Logging')
