
import requests

def send_post_request(url, data):
    try:
        # Ensure that the URL is using http:// or https://
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # Raises an error for bad responses
        return response.json()  # Return JSON response
    except requests.exceptions.ConnectionError as e:
        print(f"ConnectionError: {e}")
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")

# Example data and URL
url = "http://example.com/api"
data = {"key": "value"}
send_post_request(url, data)
