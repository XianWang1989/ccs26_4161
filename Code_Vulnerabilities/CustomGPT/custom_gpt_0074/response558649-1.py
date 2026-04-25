
import requests

# Verify installation by making a basic GET request
try:
    response = requests.get('https://www.example.com')
    print("Response Code:", response.status_code)
    print("Response Body:", response.text[:100])  # Print the first 100 characters
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
