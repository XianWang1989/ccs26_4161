
import requests

response = requests.post('http://your.api.endpoint', data={'key': 'value'}, headers={'Host': 'example.com'})
print(response.status_code)
