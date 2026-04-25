
import requests

try:
    # Make a secure HTTP GET request
    response = requests.get('https://api.github.com', timeout=5)
    response.raise_for_status()  # Raise an error for bad responses
    print("Response from GitHub API:", response.json())
except requests.ConnectionError:
    print("Error: Failed to connect to GitHub API")
except requests.Timeout:
    print("Error: The request timed out")
except requests.HTTPError as err:
    print(f"HTTP Error: {err}")
except Exception as e:
    print(f"An error occurred: {e}")
