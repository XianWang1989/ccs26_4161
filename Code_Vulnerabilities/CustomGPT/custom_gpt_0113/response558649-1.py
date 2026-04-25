
import requests

url = "https://api.example.com/data"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()  # Parse JSON response
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
