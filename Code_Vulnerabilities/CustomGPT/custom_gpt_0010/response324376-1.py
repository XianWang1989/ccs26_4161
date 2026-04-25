
import requests

response = requests.post('http://external-server/api', data={'key': 'value'})
print(response.status_code, response.text)
