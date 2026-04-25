
import requests

def make_secure_request(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

data = make_secure_request("https://api.example.com/data")
print(data)
