
import requests

# Example HTTPS request
try:
    response = requests.get('https://api.github.com', timeout=5)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
