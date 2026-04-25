
import requests

# Ensure the URL is correct and reachable
url = "http://your-external-server/api/endpoint"
data = {"key": "value"}

# Make the POST request
try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
