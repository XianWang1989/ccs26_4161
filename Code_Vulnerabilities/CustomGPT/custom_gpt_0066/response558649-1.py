
import requests

url = "https://api.example.com/data"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad responses
    data = response.json()       # Assuming the API returns JSON
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
