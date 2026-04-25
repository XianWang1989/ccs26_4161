
import requests

# Example of making a secure HTTPS request
url = "https://api.github.com"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    print(response.json())  # Print the JSON response
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
