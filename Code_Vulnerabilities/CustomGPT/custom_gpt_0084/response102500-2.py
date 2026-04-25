
import google.cloud.logging
from google.cloud.logging import DESCENDING

# Initialize the Google Cloud Logging client
client = google.cloud.logging.Client()
client.setup_logging()

# Now logging will automatically send to Google Cloud Logging
logging.debug('This is a test log message.')
