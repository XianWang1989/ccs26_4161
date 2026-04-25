
import requests

def send_post_request(url, data):
    try:
        # Send POST request
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Sample usage
url = "http://example.com/api/endpoint"  # Replace with your URL
data = {"key": "value"}  # Replace with your data
response = send_post_request(url, data)
print(response)
