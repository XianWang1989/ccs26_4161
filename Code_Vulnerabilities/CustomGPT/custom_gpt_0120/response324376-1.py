
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # or response.text if you prefer raw response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Usage example
url = "http://example.com/api/endpoint"
data = {"key": "value"}
send_post_request(url, data)
