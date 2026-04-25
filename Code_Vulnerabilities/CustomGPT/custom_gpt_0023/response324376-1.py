
import requests
from requests.exceptions import ConnectionError

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses (4XX, 5XX)
        return response.json()
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data = {'key': 'value'}
url = 'http://your-external-server.com/api'

result = send_post_request(url, data)
if result:
    print('Response from server:', result)
