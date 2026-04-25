
import requests

try:
    response = requests.get("https://www.google.com")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text[:100])  # Print first 100 characters
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)
except Exception as e:
    print("Error:", e)
