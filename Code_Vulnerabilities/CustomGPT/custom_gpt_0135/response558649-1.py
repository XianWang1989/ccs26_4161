
import requests

# Make a secure request to an HTTPS URL
url = 'https://api.github.com'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for HTTP errors
    print(response.json())  # Print JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
