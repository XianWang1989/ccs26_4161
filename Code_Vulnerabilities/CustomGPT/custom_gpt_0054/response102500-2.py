
from google.cloud import logging as cloud_logging

# Create the Cloud Logging client
client = cloud_logging.Client()
client.setup_logging()

# Now the logs will be sent to Google Cloud Logging
logging.info('This log will appear in Google Cloud Logging.')
