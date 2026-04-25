
import ssl
import requests

# Check available SSL context
print("Available SSL Contexts:")
print(ssl._ssl.PROTOCOL_TLS)

# Make a test request
try:
    response = requests.get('https://www.example.com')
    print("Response Status Code:", response.status_code)
except Exception as e:
    print("Error:", e)
