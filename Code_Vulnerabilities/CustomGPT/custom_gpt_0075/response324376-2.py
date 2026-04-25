
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def send_post_request():
    try:
        logging.debug("Sending POST request to external server...")
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "foo", "body": "bar", "userId": 1})
        response.raise_for_status()  # Raise an error for bad responses
        logging.debug("Response received: %s", response.json())
    except requests.exceptions.RequestException as e:
        logging.error("Request failed: %s", e)

send_post_request()
