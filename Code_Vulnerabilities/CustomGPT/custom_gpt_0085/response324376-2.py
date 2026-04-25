
import logging

logger = logging.getLogger(__name__)

try:
    response = requests.post('http://your_external_server/v1/resource', data={'key': 'value'})
except requests.ConnectionError as e:
    logger.error(f"Connection error: {e}")
