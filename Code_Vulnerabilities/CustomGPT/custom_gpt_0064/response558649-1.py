
import requests

# Make a secure request
try:
    response = requests.get('https://api.github.com', timeout=5)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(response.json())  # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
