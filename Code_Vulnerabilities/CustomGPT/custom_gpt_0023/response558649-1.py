
import requests

try:
    response = requests.get('https://api.github.com')
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print("Success:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
