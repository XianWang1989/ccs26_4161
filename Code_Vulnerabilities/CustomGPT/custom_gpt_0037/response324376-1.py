
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data, timeout=10)  # Set timeout
        response.raise_for_status()  # Raise an error for bad responses
        print('Response:', response.json())
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)

# Usage
data = {'key': 'value'}
send_post_request('http://example.com/api', data)
