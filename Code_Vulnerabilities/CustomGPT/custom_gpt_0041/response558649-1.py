
import requests

# Make a secure GET request
try:
    response = requests.get('https://example.com', timeout=10)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())  # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
