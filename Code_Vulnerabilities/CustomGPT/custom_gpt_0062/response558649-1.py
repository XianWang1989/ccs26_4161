
import requests

# Check the installed version
print("Requests version:", requests.__version__)

# Test a secure connection
try:
    response = requests.get('https://www.example.com')
    print("Response status code:", response.status_code)
except requests.exceptions.SSLError as e:
    print("SSL error occurred:", e)
