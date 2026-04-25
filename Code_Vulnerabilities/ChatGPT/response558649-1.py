
import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # Check for HTTP errors
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error during requests to example.com: {e}")
