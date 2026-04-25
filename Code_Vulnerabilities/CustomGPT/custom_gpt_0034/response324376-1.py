
import requests

url = 'http://your.api.endpoint'
response = requests.post(url, json={"key": "value"}, headers={"Content-Type": "application/json"})
