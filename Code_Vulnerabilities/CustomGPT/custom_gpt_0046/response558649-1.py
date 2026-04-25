
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())  # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
