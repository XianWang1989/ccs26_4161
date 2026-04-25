
import requests

response = requests.post(
    'http://your_external_server_ip/v1/resource', 
    data={'key': 'value'}
)
