
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, data=data, headers={'Connection': 'keep-alive'}, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the response is JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Usage
url = 'http://example.com/api/endpoint'
data = {'key': 'value'}

response = send_post_request(url, data)
print(response)
