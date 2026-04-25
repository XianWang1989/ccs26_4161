
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()  # Assuming the response contains JSON
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        raise

# Example usage
url = 'http://example.com/api'  # Replace with your actual URL
data = {'key': 'value'}  # Replace with your actual data

send_post_request(url, data)
