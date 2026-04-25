
import requests

# Example of making a secure request
try:
    response = requests.get('https://api.github.com', verify=True)
    print(response.json())
except requests.exceptions.SSLError as e:
    print(f"SSL Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
