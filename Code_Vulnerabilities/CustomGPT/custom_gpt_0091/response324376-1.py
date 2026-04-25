
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send POST request: {e}")
        raise

# Example usage
url = "http://example.com/api"
data = {"key": "value"}

send_post_request(url, data)
