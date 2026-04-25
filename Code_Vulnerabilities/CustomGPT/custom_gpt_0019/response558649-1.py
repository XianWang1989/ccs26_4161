
import requests

try:
    response = requests.get('https://api.github.com')
    response.raise_for_status()  # Check for HTTP errors
    print(response.json())  # Output the JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
