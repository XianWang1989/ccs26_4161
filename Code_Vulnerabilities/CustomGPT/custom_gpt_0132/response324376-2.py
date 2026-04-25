
import logging
import requests

logging.basicConfig(level=logging.DEBUG)

try:
    response = requests.post('http://external-server.com/api', data={'key': 'value'})
    print(response.content)
except requests.ConnectionError as e:
    logging.error(f'Connection failed: {e}')
