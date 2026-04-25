
import requests

try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
