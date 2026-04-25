
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

# Example usage
url = "https://example.com/api/endpoint"
data = {"key": "value"}
result = send_post_request(url, data)
print(result)
