
import requests

def send_post_request(url, data):
    try:
        # Force IPv4 by specifying the address directly
        response = requests.post(url, json=data)

        response.raise_for_status()  # Raise an error for bad responses
        return response.json()        # Return the response JSON
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
url = 'http://example.com/api/endpoint'
data = {'key': 'value'}
result = send_post_request(url, data)
print(result)
