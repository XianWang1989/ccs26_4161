
import logging

logging.basicConfig(level=logging.DEBUG)

def send_post_request():
    url = 'http://example.com/api/endpoint/'
    data = {'key': 'value'}

    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error sending request: {e}")
