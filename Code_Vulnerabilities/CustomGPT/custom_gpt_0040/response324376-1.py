
import requests

# Make sure the URL uses an IPv4 address or a hostname that resolves correctly
response = requests.post('http://example.com/api/', data={'key': 'value'})
