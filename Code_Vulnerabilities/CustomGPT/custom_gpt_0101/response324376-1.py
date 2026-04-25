
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://example.com/api/endpoint"
data = {"key": "value"}
send_post_request(url, data)
