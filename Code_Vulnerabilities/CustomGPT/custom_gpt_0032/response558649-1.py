
import requests

try:
    response = requests.get('https://example.com', verify=True)
    print("Response Status Code:", response.status_code)
except requests.exceptions.SSLError as e:
    print("SSL Error:", e)
