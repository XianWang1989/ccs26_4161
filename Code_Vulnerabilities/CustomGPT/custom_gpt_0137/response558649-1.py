
import requests
from requests.exceptions import RequestException

# Check and handle SSL warnings
try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Raise an error for bad responses
    print(response.text)
except RequestException as e:
    print(f"An error occurred: {e}")
