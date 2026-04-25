
import sys
import requests

print("Python version:", sys.version)
try:
    response = requests.get('https://api.github.com')
    print("Response Status Code:", response.status_code)
except Exception as e:
    print("Error:", e)
