
import requests

def send_post_request(data, url):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Process the response as needed
    except requests.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")

# Usage
url = 'http://example.com/api/endpoint'  # Make sure this URL is using the correct address family (IPv4)
data = {'key': 'value'}
send_post_request(data, url)
