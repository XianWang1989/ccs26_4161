
import requests

# Check Python version
import sys
print("Python version:")
print(sys.version)

# Use requests
try:
    response = requests.get("https://httpbin.org/get")
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)
