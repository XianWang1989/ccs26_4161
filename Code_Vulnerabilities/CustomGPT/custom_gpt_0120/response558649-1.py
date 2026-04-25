
import requests

try:
    response = requests.get('https://api.github.com')
    response.raise_for_status()  # Raise an error for bad responses
    print("Response received successfully:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
