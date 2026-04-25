
import requests

def send_post_request(url, data):
    try:
        # Force the use of IPv4
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'}, timeout=10)
        response.raise_for_status()  # Raises an error for HTTP errors
        return response.json()
    except requests.ConnectionError as e:
        print(f"Connection error: {e}")
    except requests.Timeout as e:
        print(f"Timeout error: {e}")
    except requests.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
data = {'key': 'value'}
url = 'http://example.com/api'  # Replace with your URL
send_post_request(url, data)
