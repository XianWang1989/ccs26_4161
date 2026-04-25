
import requests

try:
    response = requests.get('https://www.example.com')
    response.raise_for_status()  # Raise an error for bad responses
    print(response.content)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
