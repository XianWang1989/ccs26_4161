
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def send_post_request(url, data):
    try:
        logging.debug(f'Sending POST request to {url} with data: {data}')
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for HTTP errors
        logging.debug(f'Response: {response.status_code} - {response.text}')
        return response.json()
    except requests.exceptions.ConnectionError as e:
        logging.error(f'ConnectionError: {e}')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

# Example usage
url = 'http://external-server/api'
data = {'key': 'value'}
send_post_request(url, data)
