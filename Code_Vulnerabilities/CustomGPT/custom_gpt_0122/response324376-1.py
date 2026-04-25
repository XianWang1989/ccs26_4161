
import requests

url = 'http://example.com/api'
# Use IPv4 explicitly if needed
response = requests.post(url, data={'key': 'value'}, headers={'Host': 'example.com'})

print(response.status_code)
