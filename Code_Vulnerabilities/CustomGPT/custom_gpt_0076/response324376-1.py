
import requests

def send_post_request(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Example usage
url = "http://external-server.com/api"
data = {"key": "value"}
send_post_request(url, data)
