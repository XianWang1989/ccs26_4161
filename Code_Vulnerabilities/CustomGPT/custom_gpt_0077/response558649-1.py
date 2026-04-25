
import requests

# Example GET request
url = "https://api.example.com/data"
response = requests.get(url)

# Handle potential exceptions
try:
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()  # Parse JSON response
    print(data)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as exc:
    print(f"An error occurred: {exc}")
